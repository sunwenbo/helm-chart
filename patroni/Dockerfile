FROM registry.opensource.zalan.do/acid/spilo-10:1.5-p5
RUN echo "ulimit -c 0" >> /root/.bashrc
RUN ulimit -c 0
CMD ["/bin/sh", "/launch.sh"]
