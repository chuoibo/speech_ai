import logging

from src.schema.speech_system_schema import InputSpeechSystemModel
from src.module.sys_pipeline import SpeechSystem
from src.celery_tasks.app_worker import app


@app.task(name='speech_ai')
def speech_ai(input_data):
    live_record = input_data.get("live_record")
    
    inp = InputSpeechSystemModel(
        live_record=live_record,
    )
    
    result = SpeechSystem(inp=inp).run()
    logging.info('Implementing speech task...')
    return result.dict()

