#!/usr/bin/env bash
# -*- coding: utf-8 -*-

DEPLOY_DIR="$HOME/workspace/hacktiv8/ftds_learning_journal/phase_2/week_3/tf_serving/deploy_motogp"

docker run -it --rm \
    -p 8500:8500 -p 8501:8501 \
    -v "$DEPLOY_DIR/models/motogp:/models/motogp" \
    -e MODEL_NAME=motogp \
    -t tensorflow/serving
