from __future__ import annotations

import re

from functools import lru_cache

def get_model_fields(model: type[BaseModel]) -> list[ModelField]:
    model_fields: list[ModelField] = []
    for name, field_info in model.model_fields.items():
        type_ = field_info.annotation
        if lenient_issubclass(type_, (BaseModel, dict)) or is_dataclass(type_):
            model_config = None
        else:
            model_config = model.model_config
        model_fields.append(
            ModelField(
                field_info=field_info,
                name=name,
                config=model_config,
            )
        )
    return model_fields

def get_flat_models_from_model(
    model: type["BaseModel"], known_models: TypeModelSet | None = None
) -> TypeModelSet:
    known_models = known_models or set()
    fields = get_model_fields(model)
    get_flat_models_from_fields(fields, known_models=known_models)
    return known_models

def get_flat_models_from_annotation(
    annotation: Any, known_models: TypeModelSet
) -> TypeModelSet:
    origin = get_origin(annotation)
    if origin is not None:
        for arg in get_args(annotation):
            if lenient_issubclass(arg, (BaseModel, Enum)):
                if arg not in known_models:
                    known_models.add(arg)  # type: ignore[arg-type]
                    if lenient_issubclass(arg, BaseModel):
                        get_flat_models_from_model(arg, known_models=known_models)
            else:
                get_flat_models_from_annotation(arg, known_models=known_models)
    return known_models

def get_flat_models_from_field(
    field: ModelField, known_models: TypeModelSet
) -> TypeModelSet:
    field_type = field.field_info.annotation
    if lenient_issubclass(field_type, BaseModel):
        if field_type in known_models:
            return known_models
        known_models.add(field_type)
        get_flat_models_from_model(field_type, known_models=known_models)
    elif lenient_issubclass(field_type, Enum):
        known_models.add(field_type)
    else:
        get_flat_models_from_annotation(field_type, known_models=known_models)
    return known_models

def get_flat_models_from_fields(
    fields: Sequence[ModelField], known_models: TypeModelSet
) -> TypeModelSet:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')
