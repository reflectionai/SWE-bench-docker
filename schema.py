import pydantic


class AllPreds(pydantic.BaseModel):
  model_name_or_path: str
  instance_id: str
  model_patch: str

  class Config:
    protected_namespaces = ()


class DataPoint(pydantic.BaseModel):
  model_config = pydantic.ConfigDict(extra='ignore')
  instance_id: str
  patch: str
