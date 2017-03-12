uses tests;

{ Дан массив целых чисел.
  Выдать все числа, входящие в массив по одному разу. }


function getUnique(a: array of integer): array of integer;
begin
  // ...
  result := a;
end;


begin
  task1(getUnique);
end.