import subprocess as sp

import click
from openai import OpenAI


@click.command()
@click.argument("question")
@click.option("-m", "--model", default="gpt-3.5-turbo")
def ask(question, model):
    """Ask ChatGPT a question."""
    secret_ref = "op://Private/openai-api-key/credential"

    process = sp.run(
        ["op", "read", secret_ref],
        capture_output=True,
        text=True,
        check=True,
    )

    api_key = process.stdout.strip()

    client = OpenAI(api_key=api_key)

    stream = client.chat.completions.create(
        messages=[{"role": "user", "content": question}],
        model=model,
        stream=True,
    )

    for part in stream:
        print(part.choices[0].delta.content or "", end="")
