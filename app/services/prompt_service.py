from pathlib import Path


class PromptService:

    def load_prompt(
        self,
        prompt_name: str,
    ) -> str:

        prompt_path = (
            Path("app/prompts")
            / prompt_name
        )

        return prompt_path.read_text()