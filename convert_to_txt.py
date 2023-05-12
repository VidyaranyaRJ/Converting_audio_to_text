import asyncio
from dotenv import load_dotenv
from deepgram import Deepgram

load_dotenv()
deepgram_api_key = "0bd503559ed27813807ee47f0a9fdaeaf1d15d2e"
async def main():
    deepgram = Deepgram(deepgram_api_key)
    with open('Speaker McCarthy Says President Biden Is Ignoring Debt-Limit Issue.mp4', 'rb') as audio:
        source = { 'buffer' : audio, 'mimetype' : 'video/mp4' }
        transcription_option = { 'punctuate' : True, 'diariaze' : True, 'paragraphs' : True }
        response = await deepgram.transcription.prerecorded(source, transcription_option)
        transript = response['results']['channels'][0]['alternatives'][0]['paragraphs']['transcript']
        with open('audio_to_text.txt', 'w') as f:
            f.write(transript)
        print(response)

if __name__ == '__main__':
    asyncio.run(main())