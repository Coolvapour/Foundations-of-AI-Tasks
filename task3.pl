% Unit: CCS 2226 Foundations of AI
% Student Name: Moses Kiprono Leleito
% Registration Number: CIT-227-073/2024
% Task: Practical Task Three - Prolog Family Tree

% --- Facts: Parents ---
% parent(Parent, Child)
parent(john, moses).
parent(john, sarah).
parent(mary, moses).
parent(mary, sarah).

parent(peter, john).
parent(ann, john).
parent(peter, james).
parent(ann, james).

parent(james, kevin).
parent(linda, kevin).

% --- Facts: Gender ---
male(john).
male(peter).
male(moses).
male(james).
male(kevin).
female(mary).
female(ann).
female(sarah).
female(linda).

% --- Rules ---

% Grandparent Rule: GP is a grandparent of GC if GP is a parent of P, and P is a parent of GC.
grandparent(GP, GC) :-
parent(GP, P),
parent(P, GC).

% Sibling Rule: X and Y are siblings if they share a parent P, and X is not the same person as Y.

sibling(X, Y) :-
parent(P, X),
parent(P, Y),
X \= Y.

% Uncle/Aunt Rule: UA is an uncle or aunt of N if UA is a sibling of N's parent P.
uncle_or_aunt(UA, N) :-
sibling(UA, P),
parent(P, N).

% Cousin Rule: X and Y are cousins if their parents (PX and PY) are siblings.
cousin(X, Y) :-
parent(PX, X),
parent(PY, Y),
sibling(PX, PY).

% --- Practical Logic Queries for Tested: ---

% grandparent(peter, moses).
% uncle_or_aunt(james, moses).
% cousin(moses, kevin).
% sibling(moses, sarah).