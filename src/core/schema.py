from pydantic import BaseModel, Field

class Word(BaseModel):
    word: str    = Field("")
    start: float = Field(0, description = "Time start (second)")
    end: float   = Field(0, description = "Time end (second)")
   
class SenseUnits(BaseModel):
    level: str = Field(
        "", 
        description = (
            "Represent chunking levels:\n",
            "  (1) minimal: minimal sense unit, including unclosed but locally stable phrase, the most aggressive and lowest latency, good for simultaneous asr\n",
            "  (2) phrase:  less aggressive and more latency, balanced with latency and accuracy than minimal\n",
            "  (3) clause:  balanced with latency and accuracy, good for simultaneous sound to text translation\n",
            "  (4) sentence: for high accuracy purposes but latency is high, not good for simultaneous tasks"
            )
        )
    groups: list[list[int]] = Field(default_factory = lambda: [[]], description = "Word indices grouped into sense units")

class Mapping(BaseModel):
    target_senseunit_id: int = Field(-1)
    source_token_ids: list[int]  = Field(default_factory = list)

class Translation(BaseModel):
    uid: str                 = Field(...)
    language: str            = Field(...)
    raw_translation: str     = Field("", description = "Raw translation text. This is only used for comparison and will not used for downstream procedures")
    text: str                = Field("", description = "Reconstructed translation text")
    tokens: list[str]        = Field(default_factory = list, description = "List of words")
    sense_units: SenseUnits  = Field(default_factory = lambda: SenseUnits(level = "minimal"))
    mappings: list[Mapping]  = Field(default_factory = lambda: [],  description = "Mapping_1, Mapping_2, ...; Mapping_i = Mapping(target_senseunit_id = ..., source_token_ids = [...])")
    max_empty_window: int    = Field(999)
    score: float             = Field(0.0)
    author: str              = Field("")

class Transcription(BaseModel):
    uid: str          = Field(...)
    language: str     = Field(...)
    text: str         = Field("" , description = "Transcription.")
    tokens:list[Word] = Field(default_factory = list,description = "Character-level alignment (based on ZH, JA, KO)")
    words: list[list[int]]  = Field(default_factory = lambda: [[]],  description = "Token indices grouped into words")
    sense_units: SenseUnits = Field(default_factory = lambda: SenseUnits(level = "minimal"))
    score: float      = Field(0.0, description = "Transcription score. This score is graded with LLM, only depends on if the transcription is well-structured and logical or not")
    author: str       = Field("")

class Chunk(BaseModel):
    start: float      = Field(..., description = "Start time of chunk (second)")
    end: float        = Field(..., description = "End time of chunk (second)")
    words: list[Word] = Field(default_factory = list,  description = "Words with indices")

class AudioMetaData(BaseModel):
    id: str            = Field(...)
    file_name: str     = Field(...)
    duration: float    = Field(..., description = "Duration time (seconds).")
    sample_rate: float = Field(..., description = "The original sample rate of the audio clip.")
    transcription: Transcription = Field(...)
    translations: dict[str, Translation] = Field(default_factory = dict, description = "dict type: {\"lang\": Translation}")

class MetaData(BaseModel):
    uid: str           = Field(...)
    file_name: str     = Field(...)
    duration: float    = Field(..., description = "Duration time (seconds).")
    sample_rate: float = Field(..., description = "The original sample rate of the audio clip.")
    language: str      = Field(...)
    subset: str        = Field("")
    quality: float     = Field(float("nan"))
