# Sea Battle Modes

Режимы игры для проекта "Морской бой"

## Функциональность

- Базовый класс Game для управления игрой
- Режим игры вдвоём (TwoPlayerGame)
- Искусственный интеллект (BotPlayer)
- Режим игры с компьютером (SinglePlayerGame)

## Установка

```bash
git clone https://github.com/ваш-логин/sea-battle-modes.git

Использование
python
from game_modes import SinglePlayerGame,TwoPlayerGame

# Игра с ботом
game=SinglePlayerGame(difficulty="medium")

# Игра с другом
game=TwoPlayerGame()

Автор: Кирилл Денисов
