import pandas as pd

from pydantic import BaseModel, model_validator


class QCode(BaseModel):
    code: str
    question: str
    answer: str

    def check(self, provided_code: str) -> bool:
        if len(provided_code) == 2:
            _provided_code = f"Q{provided_code.upper()}"
        _provided_code = provided_code.upper()
        return _provided_code == self.code


class QCodeLanguage(BaseModel):
    web: str
    full: list[QCode] = None
    voice: list[QCode] = None
    short: list[QCode] = None

    _short_codes: set = {
        "QRA",
        "QRB",
        "QRD",
        "QRE",
        "QRF",
        "QRG",
        "QRH",
        "QRI",
        "QRL",
        "QRM",
        "QRN",
        "QRO",
        "QRP",
        "QRQ",
        "QRR",
        "QRS",
        "QRT",
        "QRU",
        "QRV",
        "QRW",
        "QRX",
        "QRY",
        "QRZ",
        "QSA",
        "QSG",
        "QSL",
        "QSM",
        "QSN",
        "QSO",
        "QSP",
        "QSR",
        "QSS",
        "QSU",
        "QSV",
        "QSW",
        "QSX",
        "QSY",
        "QSZ",
        "QTH",
        "QTR",
        "QTX",
    }

    @model_validator(mode="before")
    def populate_full_language(cls, values):
        data = pd.read_html(values["web"])[0]
        data.columns = ["code", "question", "answer"]
        values["full"] = [QCode(**q) for q in data.to_dict(orient="records")]
        return values

    @model_validator(mode="after")
    def populate_voice_language(cls, values):
        values.voice = [q for q in values.full if q.code[1] in ["R", "S"]]
        return values

    @model_validator(mode="after")
    def populate_short_language(cls, values):
        values.short = [q for q in values.full if q.code in values._short_codes]
        return values
