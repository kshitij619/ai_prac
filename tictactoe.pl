win(Player, Board) :-
    (Board = [Player, Player, Player, _, _, _, _, _, _]);
    (Board = [_, _, _, Player, Player, Player, _, _, _]);
    (Board = [_, _, _, _, _, _, Player, Player, Player]);
    (Board = [Player, _, _, Player, _, _, Player, _, _]);
    (Board = [_, Player, _, _, Player, _, _, Player, _]);
    (Board = [_, _, Player, _, _, Player, _, _, Player]);
    (Board = [Player, _, _, _, Player, _, _, _, Player]);
    (Board = [_, _, Player, _, Player, _, Player, _, _]).

free(Position, Board) :-
    nth0(Position, Board, empty).

winning_move(Board, Player, Move) :-
    free(Move, Board),nth0(Move, Board, Player, NewBoard), win(Player, NewBoard).

blocking_move(Board, Move) :-
    winning_move(Board, o, Move).

center_move(Board, Move) :-
    nth0(4, Board, empty), Move = 4.

corner_move(Board, Move) :-
    member(Move, [0, 2, 6, 8]), nth0(Move, Board, empty).

first_available(Board, Move) :-
    nth0(Move, Board, empty).

best_move(Board, Move) :-
    (winning_move(Board, x, Move), !);
    (blocking_move(Board, Move), !);
    (center_move(Board, Move), !);
    (corner_move(Board, Move), !);
    first_available(Board, Move).

% how to run
% best_move([o,x,o,empty, x, empty, empty,empty, empty], Move)
