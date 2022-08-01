FROM tensorflow/serving

ENV MODEL_BASE_PATH /models
ENV MODEL_NAME motogp

COPY models /models

COPY tf_serving_entrypoint.sh /usr/local/bin/tf_serving_entrypoint.sh
RUN chmod +x /usr/local/bin/tf_serving_entrypoint.sh
ENTRYPOINT []
CMD ["/usr/local/bin/tf_serving_entrypoint.sh"]

