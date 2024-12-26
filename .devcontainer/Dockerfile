FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    git \
    curl \
    gcc \
    g++ \
    postgresql-client \
    redis-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Configuration de l'environnement de développement
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN chown -R $USERNAME:$USERNAME /usr/local/* \
    && chown -R $USERNAME:$USERNAME /workspace 

USER $USERNAME

RUN pip install uv

# Préparation des ports
EXPOSE 8000 8501 8888 