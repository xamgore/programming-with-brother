uses tests;

{ ��� ������ ����� �����.
  ���������� ���������� ��������� � �������� ������� ������
    �� ������ ������ �����. }
  

function maxSeqOfZeros(a: array of integer): integer;
begin
  // ...
  result := 0;
end;


begin
  var arr: array of integer := (7, 4, 0, 0, 5, 7, 0, 7);
  writeln(maxSeqOfZeros(arr));

  // task5(maxSeqOfZeros);
end.