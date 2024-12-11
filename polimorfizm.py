class ChessPiece:
    def __init__(self, horizontal: str, vertical: int):
        if horizontal not in 'abcdefgh':
            raise ValueError("Горизонтальная координата должна быть буквой от a до h.")
        if vertical < 1 or vertical > 8:
            raise ValueError("Вертикальная координата должна быть целым числом от 1 до 8.")

        self.horizontal = horizontal
        self.vertical = vertical

    def can_move(self, target_horizontal: str, target_vertical: int) -> bool:
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах.")


class King(ChessPiece):
    def can_move(self, target_horizontal: str, target_vertical: int) -> bool:
        horizontal_diff = abs(ord(target_horizontal) - ord(self.horizontal))
        vertical_diff = abs(target_vertical - self.vertical)
        return (horizontal_diff <= 1 and vertical_diff <= 1)


class Knight(ChessPiece):
    def can_move(self, target_horizontal: str, target_vertical: int) -> bool:
        horizontal_diff = abs(ord(target_horizontal) - ord(self.horizontal))
        vertical_diff = abs(target_vertical - self.vertical)
        return (horizontal_diff == 2 and vertical_diff == 1) or (horizontal_diff == 1 and vertical_diff == 2)


king = King('e', 1)
knight = Knight('g', 1)

king_moves = [('e', 2), ('d', 1), ('f', 1), ('d', 2), ('e', 3)]
print("Король:")
for move in king_moves:
    target_horizontal, target_vertical = move
    print(
        f"Может ли король переместиться на {target_horizontal}{target_vertical}? {king.can_move(target_horizontal, target_vertical)}")

knight_moves = [('e', 2), ('h', 3), ('f', 2), ('e', 3), ('h', 2)]
print("\nКонь:")
for move in knight_moves:
    target_horizontal, target_vertical = move
    print(
        f"Может ли конь переместиться на {target_horizontal}{target_vertical}? {knight.can_move(target_horizontal, target_vertical)}")
