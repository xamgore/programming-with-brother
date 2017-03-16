uses tests;

{ Дан массив целых чисел.
  Определить, сколько раз в массиве меняется знак. }
  

function howMuch(a: array of integer): integer;
begin
  // ...
  result := 0;
end;


begin
  var arr: array of integer := (7, -4, 0, 0, -5, 7, 0, -7);
  writeln(howMuch(arr));

  // task6(howMuch);
end.