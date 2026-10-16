---
name: audio
description: Use Kitsch Labs MCP to list voices, synthesize speech, transcribe an authorized local audio file, manage audio streams, or recover an existing audio operation. Use when the user requests Kitsch audio tools; for implementing an HTTP API integration in an application, use the API documentation instead.
---

# Kitsch audio

Use the connected Kitsch MCP tools and their actual schemas. Tool names may have
a client-added prefix. Discover the tools available under the user's approved
permissions; never invent a tool or argument.

## Connection and scope

If disconnected, follow the client's authentication flow for the installed Kitsch
plugin at `https://mcp.kitschlabs.com/mcp`. Let the user complete account sign-in,
workspace selection, and consent in their browser. Never request passwords or
API keys in chat. The selected active workspace requires owner or admin access.

Preserve other MCP connections. Do not add a second manual Kitsch server when
the plugin already provides one. Installation or login is not authorization for
a paid audio test. Confirm setup with tool discovery and `list_voices`.

For application development, read
[the HTTP API integration guide](https://www.kitschlabs.com/docs/en/for-agents#service-api).
Do not install MCP merely to implement an application's API client.

## Paid work

Synthesis and transcription use the selected workspace's credits or postpaid
usage. Follow the user's requested input and approved scope. If voice, input,
or batch size is unclear, resolve that before starting; do not invent prices.
For live testing, agree on inputs, request count, and spending limit first.
Do not generate an extra sample just to verify installation.

Create one operation ID per new synthesis or transcription and retain it with
the request ID and result until delivery. Use the current Unix milliseconds and
a fresh UUIDv4, for example:

```javascript
const operation_id = Date.now() + "_" + crypto.randomUUID();
```

Never use a fixed example or a bare UUID. Omit optional fields when unset.

## Synthesize speech

1. Call `list_voices` and select a returned `voice_id` matching the user's choice.
   Do not guess IDs from names.
2. Call `synthesize_speech` with `voice_id`, authorized `text`, and `operation_id`.
   MP3 is the default; use `output_format: "wav"` when WAV is requested.
3. Deliver the returned download link and MIME type. Treat the link as private.
   Links last up to 15 minutes and files are retained for 24 hours; use
   `get_audio_operation` for a fresh link within retention.
   Optional `return_audio: true` includes new results up to 2 MiB; recovery uses links.
   Do not claim playback or delivery until it has actually been checked.

## Transcribe a file

A remote MCP server cannot read a local path. A file-capable shell or HTTP tool
must be available; otherwise explain this limitation.

1. Use only the audio file the user authorized. Read its filename and actual size;
   the maximum is 100 MiB.
2. Call `prepare_transcription` with `operation_id`, `filename`, and `size_bytes`.
   This prepares an upload; it does not upload or transcribe the file.
3. Send the file with the returned `method`, `upload_url`, `headers`,
   `multipart_fields`, and `file_field`. Confirm the upload destination is the
   expected Kitsch service before sending audio or credentials. Do not forward
   credentials to an unrelated host or stage audio on a file-sharing service.
   Keep upload credentials out of chat and shell logs; they are single-use
   and expire after five minutes.
4. Deliver the transcript and retain the operation ID for recovery.

Do not pass `audio_url` or use the local stdio `transcribe_audio` tool on the
hosted server. Omit `language` and `prompt` when unspecified.

## Recover without repeating paid work

On a timeout or lost response, call `get_audio_operation` with the original ID.
An `unknown` result does not prove that nothing ran or was billed. Report what
is known and keep the request ID; do not automatically create a new operation,
resubmit synthesis, or upload the file again. Respect any
`admission_blocked_until` returned by the server. Cancellation and disconnection
do not undo started work or charges.

## Stream speech or transcription

Discover `create_audio_stream`, `get_audio_stream`, and `close_audio_stream` before
using them. A WebSocket-capable client is required to send and receive audio.

1. Call `create_audio_stream` with a new `operation_id` and `kind: "tts"` or
   `kind: "stt"`. For TTS, also pass a `voice_id` from `list_voices`.
2. Connect to the returned Kitsch `websocket_url` with its one-use `headers`
   before `connect_before`. Keep credentials out of chat and logs. Use the
   returned audio format and session limit. Do not add an API key or OAuth token.
3. For TTS, send `text` and `flush` messages and consume `audio`/`isFinal` events.
   For STT, send native session, audio append, and commit events and consume
   transcription events. Audio is PCM16 LE, 24 kHz, mono. Speech output may take
   time to arrive after text submission.
4. Close the WebSocket or call `close_audio_stream`. Use `get_audio_stream` to
   distinguish transport closure from usage settlement. `recovery_required`
   means usage is uncertain; do not automatically replay input or reconnect.

After a lost preparation response, reuse the same operation ID. Repeated
preparation rotates an unused credential without extending its deadline; a
connected or ended stream is never restarted. Stream status does not retain
audio or transcripts. These tools do not configure microphones, speakers, or
the agent's default voice provider.

For current contracts and connection help, read
[the hosted MCP guide](https://www.kitschlabs.com/docs/en/mcp).
