# Sea Battle Modes

Режимы игры для проекта "Морской бой"

## Функциональность

- Базовый класс Game для управления игрой
- Режим игры вдвоём (TwoPlayerGame)
- Искусственный интеллект (BotPlayer)
- Режим игры с компьютером (SinglePlayerGame)

Использование
python
from game_modes import SinglePlayerGame,TwoPlayerGame

# Игра с ботом
game=SinglePlayerGame(difficulty="medium")

# Игра с другом
game=TwoPlayerGame()

Автор: Кирилл Денисов
Главный репозиторий https://github.com/southpepperbaby/Sea-Battle-Game
