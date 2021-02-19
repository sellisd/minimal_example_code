FROM gitpod/workspace-full

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
RUN pyenv install 3.9.0
RUN pyenv global 3.9.0
#
# More information: https://www.gitpod.io/docs/config-docker/
