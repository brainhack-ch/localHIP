##################################################################
# Use Ubuntu 20.04 LTS as base image
##################################################################
FROM focal-20221019 AS main

##################################################################
## Install Miniconda3 and the environment incl. ANTs/nipype/pybids
##################################################################
FROM main AS neurocondabuntu

# Install Miniconda3
RUN apt-get update && \
    apt-get install -qq -y --no-install-recommends curl && \
    curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -bfp /opt/conda && \
    rm -rf /tmp/miniconda.sh && \
    apt-get remove -y curl && \
    conda update conda && \
    conda clean --all --yes && \
    rm -rf ~/.conda ~/.cache/pip/* && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add conda to $PATH
ENV PATH="/opt/conda/bin:$PATH"

## Create conda environment, including ANTs 2.2.0 and MRtrix 3.0.2
ENV CONDA_ENV="py39localhip"
COPY environment.yml /app/environment.yml
RUN /bin/bash -c "conda config --set default_threads 4 &&\
    conda create env create -f /app/environment.yml &&\
    conda clean -v --all --yes &&\
    rm -rf ~/.conda ~/.cache/pip/*"

##################################################################
# Install BIDS validator
##################################################################
# RUN npm install -g bids-validator && \
#     rm -rf ~/.npm ~/.empty

##################################################################
# Installation of Connectome Mapper 3 packages
##################################################################
FROM neurocondabuntu AS localhipbuntu

# Docker build command arguments
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

# Set the working directory to /app/connectomemapper3
WORKDIR /app/localhip

# Copy Python contents of this repository.
COPY LICENSE ./LICENSE
COPY setup.py ./setup.py
COPY README.md ./README.md
COPY localhip ./localhip

# Install localhip package in the conda environment $CONDA_ENV
ENV CONDA_ENV="py39localhip"
RUN /bin/bash -c ". activate ${CONDA_ENV} &&\
    pip install ."

##################################################################
# Copy primary BIDSapp entrypoint script
##################################################################
COPY scripts/bidsapp/run_localhip.sh /app/run_localhip.sh
RUN cat /app/run_localhip.sh

##################################################################
# Acquire script to be executed
##################################################################
RUN chmod 775 /app/run.py && \
    chmod 775 /app/run_localhip.sh

##################################################################
# Create cache directory for python eggs
##################################################################
RUN mkdir -p /cache/python-eggs && \
    chmod -R 777 /cache/python-eggs

##################################################################
# Make ANTs happy
##################################################################
ENV ANTSPATH="/opt/conda/envs/${CONDA_ENV}/bin" \
    PYTHONPATH="/opt/conda/envs/${CONDA_ENV}/bin" \
    PYTHON_EGG_CACHE="/cache/python-eggs" \
    PATH="$ANTSPATH:$PATH" \
    LD_LIBRARY_PATH="/opt/conda/envs/${CONDA_ENV}/lib:${LD_LIBRARY_PATH}" \
    LD_LIBRARY_PATH="/lib/x86_64-linux-gnu:/usr/lib:/usr/local/lib:$LD_LIBRARY_PATH"

##################################################################
# Temporary tmp folder
##################################################################
RUN /bin/bash -c "mkdir -p /var/tmp"
ENV TMPDIR="/var/tmp" \
    TMP="/var/tmp" \
    TEMP="/var/tmp"

##################################################################
# Create input and output directories for BIDS App
##################################################################
RUN mkdir /bids_dir && \
    mkdir /output_dir && \
    chmod -R 777 /bids_dir && \
    chmod -R 777 /output_dir

##################################################################
# Set locale settings
##################################################################
ENV LANG="C.UTF-8" \
    LC_ALL="C.UTF-8"

##################################################################
# Unless otherwise specified each process should only use one
# thread - nipype will handle parallelization
##################################################################
ENV MKL_NUM_THREADS=1 \
    OMP_NUM_THREADS=1

##################################################################
# Run ldconfig for compatibility with Singularity
##################################################################
RUN ldconfig

##################################################################
# Show all environment variables
##################################################################
RUN export

##################################################################
# Define primary entryppoint script
##################################################################
WORKDIR /tmp/
ENTRYPOINT ["/app/run_localhip.sh"]

##################################################################
# Copy version information
##################################################################
# COPY version /version

##################################################################
# Metadata
##################################################################
LABEL org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.name="LocalHIP BIDS App" \
      org.label-schema.description="LocalHIP - Automated pipeline for electrode localization in SEEG" \
      org.label-schema.url="https://localhip.readthedocs.io" \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.vcs-url="https://github.com/brainhack-ch/localHIP" \
      org.label-schema.version=$VERSION \
      org.label-schema.maintainer="Sebastien Tourbier <sebastien.tourbier@alumni.epfl.ch>" \
      org.label-schema.vendor="Department of Clinical Neuroscience (DNC), Centre Hospitalier Universitaire Vaudois (CHUV), Lausanne, Switzerland" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.docker.cmd="docker run --rm -v ~/data/bids_dataset:/bids_dir -t XXX/localhip:${VERSION} /bids_dir /bids_dir/derivatives participant [--participant_label PARTICIPANT_LABEL [PARTICIPANT_LABEL ...]] [-session_label SESSION_LABEL [SESSION_LABEL ...]]" \
