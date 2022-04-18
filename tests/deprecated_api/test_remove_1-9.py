# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

import pytorch_lightning.loggers.base as logger_base
from pytorch_lightning.utilities.rank_zero import rank_zero_only


def test_lightning_logger_base_deprecation_warning():
    class CustomDeprecatedLogger(logger_base.LightningLoggerBase):
        def __init__(self):
            super().__init__()

        @rank_zero_only
        def log_hyperparams(self, params):
            pass

        @rank_zero_only
        def log_metrics(self, metrics, step):
            pass

        @property
        def name(self):
            pass

        @property
        def version(self):
            pass

    with pytest.deprecated_call(
        match="The `pytorch_lightning.loggers.base.LightningLoggerBase` is deprecated in v1.7"
        " and will be removed in v1.9."
    ):
        CustomDeprecatedLogger()


def test_lightning_logger_base_rank_zero_experiment_deprecation_warning():
    with pytest.deprecated_call(
        match="The `pytorch_lightning.loggers.base.rank_zero_experiment` is deprecated in v1.7"
        " and will be removed in v1.9."
    ):
        logger_base.rank_zero_experiment(None)


def test_lightning_logger_base_dummy_experiment_deprecation_warning():
    with pytest.deprecated_call(
        match="The `pytorch_lightning.loggers.base.DummyExperiment` is deprecated in v1.7 and will be removed in v1.9."
    ):
        _ = logger_base.DummyExperiment()


def test_lightning_logger_base_dummy_logger_deprecation_warning():
    with pytest.deprecated_call(
        match="The `pytorch_lightning.loggers.base.DummyLogger` is deprecated in v1.7 and will be removed in v1.9."
    ):
        _ = logger_base.DummyLogger()


def test_lightning_logger_base_merge_dicts_deprecation_warning():
    with pytest.deprecated_call(
        match="The `pytorch_lightning.loggers.base.merge_dicts` is deprecated in v1.7 and will be removed in v1.9."
    ):
        d1 = {"a": 1.7, "b": 2.0, "c": 1, "d": {"d1": 1, "d3": 3}}
        d2 = {"a": 1.1, "b": 2.2, "v": 1, "d": {"d1": 2, "d2": 3}}
        d3 = {"a": 1.1, "v": 2.3, "d": {"d3": 3, "d4": {"d5": 1}}}
        dflt_func = min
        agg_funcs = {"a": min, "v": max, "d": {"d1": sum}}
        logger_base.merge_dicts([d1, d2, d3], agg_funcs, dflt_func)