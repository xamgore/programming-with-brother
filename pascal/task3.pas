uses tests;

{ ��� ������ ����� �����.
  ��������, ������� �� � ������� ���� �� ���� ���� ����������� �����. }
  

function hasEqual(a: array of integer): boolean;
begin
  // ...
  result := false;
end;


begin
  var arr: array of integer := (7, 4, 0, 5, 7, 0, 7);
  writeln(hasEqual(arr));

  // task3(hasEqual);
end.