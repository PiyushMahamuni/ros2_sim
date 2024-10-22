FROM osrf/ros:jazzy-desktop-full

RUN sudo apt-get update && \
    sudo apt-get install -y \
    vim \
    ros-dev-tools \
    stm32flash \
    ros-jazzy-joint-state-publisher-gui && \
    rm -rf /var/lib/apt/lists/*

# create non root user
ARG USERNAME=piyush
ARG UID=2000
ARG GID=${UID}

RUN groupadd --gid ${GID} ${USERNAME} && \
    useradd -s /bin/bash --uid ${UID} --gid ${GID} -m ${USERNAME} && \
    mkdir /home/${USERNAME}/.config && \
    chown ${UID}:${GID} /home/${USERNAME}/.config

RUN apt-get update && \
    apt-get install -y sudo && \
    echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} && \
    echo ubuntu ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME} && \
    rm -rf /var/lib/apt/lists/*

ENV QT_QPA_PLATFORM=xcb
ENV QT_X11_NO_MITSHM=1
ENV NVIDIA_DRIVER_CAPABILITIES=all
ENV NVIDIA_VISIBLE_DEVICES=all

COPY bashrc /root/bashrc
RUN cat /root/bashrc >> /root/.bashrc
# USER ubuntu
COPY bashrc /home/ubuntu/.bashrc
