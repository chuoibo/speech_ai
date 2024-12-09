import os
from dotenv import load_dotenv

from src.utils.common import read_yaml_file

load_dotenv()


class Config:
    DEBUG = False
    TESTING = False

    # RabbitMQ Configuration
    RMQ_USER = os.getenv('RMQ_USER', 'guest')
    RMQ_PWD = os.getenv('RMQ_PWD', 'guest')
    MQ_URL = os.getenv('MQ_URL', f'amqp://{RMQ_USER}:{RMQ_PWD}@rabbitmq:5672/')
    
    # Redis Configuration
    REDIS_PWD = os.getenv('REDIS_PWD', '')
    REDIS_URL = os.getenv('REDIS_URL', f'redis://:{REDIS_PWD}@redis:6379/0')
    
    # Additional configurations
    LOG_DIR = "/speech/logs"
    LOG_FILEPATH = os.path.join(LOG_DIR,"celery.log")
    COMMON_DIR = "/common_dir"

    SPEECH_CONFIG_FILEPATH = '/speech/src/config/speech_cfg.yaml'


    @classmethod
    def load_config(cls):
        return read_yaml_file(cls.SPEECH_CONFIG_FILEPATH)


class Speech2TxtConfig(Config):
    config = Config.load_config()
    speech2txt_cfg = config['speech2txt']

    #For asr
    model_name = speech2txt_cfg['model_name']
    model_cache= speech2txt_cfg['model_cache']
    post_processing_task = speech2txt_cfg['post_processing_task']
    post_processing_model_cache = speech2txt_cfg['post_processing_model_cache']
    device_name = speech2txt_cfg['device_name']
    sampling_rate = speech2txt_cfg['sampling_rate']
    return_tensors = speech2txt_cfg['return_tensors']
    padding = speech2txt_cfg['padding']
    max_len_post_processing = speech2txt_cfg['max_len_post_processing']

    #For recording
    vad_mode = speech2txt_cfg['vad_mode']
    silence_limit_seconds = speech2txt_cfg['silence_limit_seconds']
    rate = speech2txt_cfg['rate']
    frame_duration = speech2txt_cfg['frame_duration']
    channels = speech2txt_cfg['channels']
    

class EmotionAnalysisConfig(Config):
    config = Config.load_config()
    emotion_analysis_cfg = config['emotion_analysis']

    model_name = emotion_analysis_cfg['model_name']
    model_cache = emotion_analysis_cfg['model_cache']
    padding = emotion_analysis_cfg['padding']
    truncation = emotion_analysis_cfg['truncation']
    return_tensors = emotion_analysis_cfg['return_tensors']
    max_length = emotion_analysis_cfg['max_length']


class LLMConfig(Config):
    config = Config.load_config()
    llm_cfg = config['llm']

    model_cache = llm_cfg['model_cache']
    return_tensors = llm_cfg['return_tensors']
    max_new_tokens = llm_cfg['max_new_tokens']
    temperature = llm_cfg['temperature']
    repetition_penalty = llm_cfg['repetition_penalty']


class Txt2SpeechConfig(Config):
    config = Config.load_config()
    txt2speech_cfg = config['txt2speech']
    ff5_tts_custom_cfg = config['ff5_tts_custom']
    DiT_cfg = config['DiT_cfg']

    remove_silence = txt2speech_cfg['remove_silence']
    output_dir = txt2speech_cfg['output_dir']
    output_file = txt2speech_cfg['output_file']
    model_name = txt2speech_cfg['model_name']
    ckpt_file = txt2speech_cfg['ckpt_file']
    vocab_file = txt2speech_cfg['vocab_file']
    speed = txt2speech_cfg['speed']
    vocoder_name = txt2speech_cfg['vocoder_name']
    vocoder_local_path = txt2speech_cfg['vocoder_local_path']
    load_vocoder_from_local = txt2speech_cfg['load_vocoder_from_local']

 
    #Config for ff5_tts
    ref_audio_neutral = ff5_tts_custom_cfg['ref_audio_neutral']
    ref_text_neutral = ff5_tts_custom_cfg['ref_text_neutral']
    # ref_audio_sad = ff5_tts_custom_cfg['ref_audio_sad']
    # ref_text_sad = ff5_tts_custom_cfg['ref_text_sad']

    #Config for DiT model
    dim = DiT_cfg['dim']
    depth = DiT_cfg['depth']
    heads = DiT_cfg['heads']
    ff_mult = DiT_cfg['ff_mult']
    text_dim = DiT_cfg['text_dim']
    conv_layers = DiT_cfg['conv_layers']