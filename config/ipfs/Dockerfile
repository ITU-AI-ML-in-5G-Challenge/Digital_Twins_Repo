FROM ipfs/kubo:latest as ipfs
# Mount initialization scripts to container-init.d. 
# These are executed sequentially and in lexicographic order, 
# after ipfs init is run and the swarm keys are copied (if the IPFS repo needs initialization), and before the IPFS daemon is started.
ADD ./ipfs-config.sh /container-init.d/ipfs-config.sh
RUN chmod a+x /container-init.d/ipfs-config.sh

ADD ./swarm.key swarm.key
# RUN chmod a+rw /data/ipfs/swarm.key

# Enforce private network settings
ENV LIBP2P_FORCE_PNET=1