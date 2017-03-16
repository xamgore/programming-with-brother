uses tests;

{ Дан массив целых чисел.
  Выдать все числа, входящие в массив по одному разу. }


function getUnique(a: array of integer): array of integer;
begin
  // ...
  result := a; // hello
end;


begin
  var arr := Seq(7, 4, 0, 5, 7, 0, 7).ToArray;
  writeln(getUnique(arr));
  writeln(seq(1).ToArray);
  // task1(getUnique);
end.