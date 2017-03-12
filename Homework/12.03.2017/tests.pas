unit tests;

interface

uses PUnit;

procedure task1(f: arrayOf<integer> -> arrayOf<integer>);
procedure task2(f: arrayOf<integer> -> integer);
procedure task3(f: arrayOf<integer> -> boolean);
procedure task4(input: arrayOf<integer>);
procedure task5(f: arrayOf<integer> -> integer);
procedure task6(f: arrayOf<integer> -> integer);
procedure task7(f: arrayOf<integer> -> integer);

procedure say(num: integer; count: integer);


implementation


var task4Dict := new SortedDictionary<integer, integer>();

procedure say(num: integer; count: integer);
begin
  if (task4Dict.ContainsKey(num)) then
    raise new Exception('Для одного числа можно только один раз вызвать say');
  
  task4Dict.Add(num, count);
end;

procedure task1(f: arrayOf<integer> -> arrayOf<integer>);
begin  
end;

procedure task2(f: arrayOf<integer> -> integer);
begin
end;

procedure task3(f: arrayOf<integer> -> boolean);
begin
end;

procedure task4(input: arrayOf<integer>);
begin
  var d := new SortedDictionary<integer, integer>();
  
  foreach var x in input do
  begin
    if d.ContainsKey(x) then
      d[x] += 1
    else
      d[x] := 1;
  end;
  
  assertEq(true, d.SequenceEqual(task4Dict));
  // todo //assertEq(d, task4Dict);
end;

procedure task5(f: arrayOf<integer> -> integer);
begin
end;

procedure task6(f: arrayOf<integer> -> integer);
begin
end;

procedure task7(f: arrayOf<integer> -> integer);
begin
end;

begin
  
end.