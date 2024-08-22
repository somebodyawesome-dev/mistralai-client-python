"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .finetuneablemodel import FineTuneableModel
from .githubrepositoryin import GithubRepositoryIn, GithubRepositoryInTypedDict
from .trainingfile import TrainingFile, TrainingFileTypedDict
from .trainingparametersin import TrainingParametersIn, TrainingParametersInTypedDict
from .wandbintegration import WandbIntegration, WandbIntegrationTypedDict
from mistralai.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


JobInIntegrationsTypedDict = WandbIntegrationTypedDict


JobInIntegrations = WandbIntegration


JobInRepositoriesTypedDict = GithubRepositoryInTypedDict


JobInRepositories = GithubRepositoryIn


class JobInTypedDict(TypedDict):
    model: FineTuneableModel
    r"""The name of the model to fine-tune."""
    hyperparameters: TrainingParametersInTypedDict
    r"""The fine-tuning hyperparameter settings used in a fine-tune job."""
    training_files: NotRequired[List[TrainingFileTypedDict]]
    validation_files: NotRequired[Nullable[List[str]]]
    r"""A list containing the IDs of uploaded files that contain validation data. If you provide these files, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in `checkpoints` when getting the status of a running fine-tuning job. The same data should not be present in both train and validation files."""
    suffix: NotRequired[Nullable[str]]
    r"""A string that will be added to your fine-tuning model name. For example, a suffix of \"my-great-model\" would produce a model name like `ft:open-mistral-7b:my-great-model:xxx...`"""
    integrations: NotRequired[Nullable[List[JobInIntegrationsTypedDict]]]
    r"""A list of integrations to enable for your fine-tuning job."""
    repositories: NotRequired[List[JobInRepositoriesTypedDict]]
    auto_start: NotRequired[bool]
    r"""This field will be required in a future release."""
    

class JobIn(BaseModel):
    model: FineTuneableModel
    r"""The name of the model to fine-tune."""
    hyperparameters: TrainingParametersIn
    r"""The fine-tuning hyperparameter settings used in a fine-tune job."""
    training_files: Optional[List[TrainingFile]] = None
    validation_files: OptionalNullable[List[str]] = UNSET
    r"""A list containing the IDs of uploaded files that contain validation data. If you provide these files, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in `checkpoints` when getting the status of a running fine-tuning job. The same data should not be present in both train and validation files."""
    suffix: OptionalNullable[str] = UNSET
    r"""A string that will be added to your fine-tuning model name. For example, a suffix of \"my-great-model\" would produce a model name like `ft:open-mistral-7b:my-great-model:xxx...`"""
    integrations: OptionalNullable[List[JobInIntegrations]] = UNSET
    r"""A list of integrations to enable for your fine-tuning job."""
    repositories: Optional[List[JobInRepositories]] = None
    auto_start: Optional[bool] = None
    r"""This field will be required in a future release."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["training_files", "validation_files", "suffix", "integrations", "repositories", "auto_start"]
        nullable_fields = ["validation_files", "suffix", "integrations"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
