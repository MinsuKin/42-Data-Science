# Use the Ubuntu Jammy image as the base image
FROM ubuntu:jammy

# Set the user to root
USER root

# Update package lists and install required packages
RUN apt update && \
    apt install -y wget bzip2 autotools-dev automake gcc build-essential libc6-dbg curl git python3.10-venv lsb-release

# Create the /opt/src directory and change to that directory
RUN mkdir -p /opt/src

# Download Valgrind source tarball
WORKDIR /opt/src
RUN wget https://sourceware.org/pub/valgrind/valgrind-3.22.0.tar.bz2

# Extract the tarball, configure, build, and install Valgrind
RUN tar -xvf valgrind-3.22.0.tar.bz2 && \
    cd valgrind-3.22.0 && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install

# Change back to the home directory
WORKDIR /root

# Run the installation script from the specified URL
RUN bash -c "$(curl -fsSL https://raw.github.com/xicodomingues/francinette/master/bin/install.sh)"


# Install OpenSSH server
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

# Set root password for SSH (change 'rootpassword' to a secure password)
RUN echo 'root:minus201' | chpasswd

# Allow root login via SSH
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

# Set the default command to run SSH daemon
CMD ["/usr/sbin/sshd", "-D"]
