#!/bin/bash

/bin/ollama serve &

pid=$!


sleep 5

echo "Загрузка модели (llama3.1)..."

ollama pull qwen3:8b

echo "Готово!"

wait $pid