uses tests;

{ Дан массив целых чисел от 0 до 1000.
  Найти число различных элементов массива. }
  

function countUnique(a: array of integer): integer;
begin
  // ...
  result := 0;
end;


begin
  var arr: array of integer := (7, 4, 0, 5, 7, 0, 7);
  writeln(countUnique(arr));

  // task2(countUnique);
end.