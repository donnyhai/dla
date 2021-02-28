mountdir="/home/donnykong/Schreibtisch/dla/docker/mount-dir/simulation"

#docker run -it -v $mountdir:/app -w /app dla:latest bash
podman run -it -v $mountdir:/app -w /app dla:latest bash
