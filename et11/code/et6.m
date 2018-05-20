%edited Egor Namakonovs script

clear all
global channels=[3 3 1 2];
global powers=[9 4 9 4];

function export_result(nav_total, nav_waiting, tav_total, tav_waiting)
  fh=fopen("octave_out.txt", "w");
  N=4;
  str1="среднее число требований: ";
  str2="среднее число ожидающих требований: ";
  str3="среднее время пребывания: ";
  str4="среднее время ожидания: ";
  for i=1:N
    str1=[str1 " " num2str(nav_total(i))];
    str2=[str2 " " num2str(nav_waiting(i))];
    str3=[str3 " " num2str(tav_total(i))];
    str4=[str4 " " num2str(tav_waiting(i))];
  endfor
  

  str1
  str2
  str3
  str4
  
  fputs(fh, str1);
  fputs(fh, str2);
  fputs(fh, str3);
  fputs(fh, str4);

  fclose(fh);
endfunction

function m=muij(i, j)
  # i - node
  # j - req_channels
  global powers;
  global channels;
  m=min(channels(i), j) * powers(i);  
endfunction

function z=zi(node_w, node_ind, entries_amt)
  z=node_w^entries_amt;
  for j=1:entries_amt
    z=z/muij(node_ind, j);
  endfor
endfunction

function p=p_unnormed(amts, nodes_w)
  p=1;
  for ind=1:length(amts)
    p=p*zi(nodes_w(ind), ind, amts(ind));
  endfor
endfunction

function main()

  trans=[ 1/9 7/18 0 1/2;
	  7/11 0 0 4/11;
	  7/12 5/12 0 0;
	  0 0 1 0];
  
  left_full=trans-eye(4,4);
  left_full=left_full';
  left=cat(1, left_full(1:3, :), ones(1, 4));
  right=[0;0;0;1];
  ws=left \ right

  Nentries=6;
  Nnodes=4;
  conditions={[6, 0, 0, 0], [5, 1, 0, 0], [5, 0, 1, 0], [5, 0, 0, 1], [4, 2, 0, 0], [4, 1, 1, 0], [4, 1, 0, 1], [4, 0, 2, 0], [4, 0, 1, 1], [4, 0, 0, 2], [3, 3, 0, 0], [3, 2, 1, 0], [3, 2, 0, 1], [3, 1, 2, 0], [3, 1, 1, 1], [3, 1, 0, 2], [3, 0, 3, 0], [3, 0, 2, 1], [3, 0, 1, 2], [3, 0, 0, 3], [2, 4, 0, 0], [2, 3, 1, 0], [2, 3, 0, 1], [2, 2, 2, 0], [2, 2, 1, 1], [2, 2, 0, 2], [2, 1, 3, 0], [2, 1, 2, 1], [2, 1, 1, 2], [2, 1, 0, 3], [2, 0, 4, 0], [2, 0, 3, 1], [2, 0, 2, 2], [2, 0, 1, 3], [2, 0, 0, 4], [1, 5, 0, 0], [1, 4, 1, 0], [1, 4, 0, 1], [1, 3, 2, 0], [1, 3, 1, 1], [1, 3, 0, 2], [1, 2, 3, 0], [1, 2, 2, 1], [1, 2, 1, 2], [1, 2, 0, 3], [1, 1, 4, 0], [1, 1, 3, 1], [1, 1, 2, 2], [1, 1, 1, 3], [1, 1, 0, 4], [1, 0, 5, 0], [1, 0, 4, 1], [1, 0, 3, 2], [1, 0, 2, 3], [1, 0, 1, 4], [1, 0, 0, 5], [0, 6, 0, 0], [0, 5, 1, 0], [0, 5, 0, 1], [0, 4, 2, 0], [0, 4, 1, 1], [0, 4, 0, 2], [0, 3, 3, 0], [0, 3, 2, 1], [0, 3, 1, 2], [0, 3, 0, 3], [0, 2, 4, 0], [0, 2, 3, 1], [0, 2, 2, 2], [0, 2, 1, 3], [0, 2, 0, 4], [0, 1, 5, 0], [0, 1, 4, 1], [0, 1, 3, 2], [0, 1, 2, 3], [0, 1, 1, 4], [0, 1, 0, 5], [0, 0, 6, 0], [0, 0, 5, 1], [0, 0, 4, 2], [0, 0, 3, 3], [0, 0, 2, 4], [0, 0, 1, 5], [0, 0, 0, 6]};
  Ps=zeros(1, length(conditions));

  cond_norm=0;
  for i=1:length(conditions)
    cond_norm=cond_norm+p_unnormed(conditions{i}, ws);
  endfor
  for i=1:length(conditions)
    Ps(i)=p_unnormed(conditions{i}, ws)/cond_norm;
  endfor

  Ps
  sum(Ps)

  nav_waiting=zeros(1, 4);
  nav_service=zeros(1, 4);
  nav_total=zeros(1, 4);
  tav_waiting=zeros(1, 4);
  tav_service=zeros(1, 4);

  global channels;
  for ci=1:length(conditions)
    cond=conditions{ci};
    Pcond=Ps(ci);
    dnav_total=cond*Pcond;
    nav_total=nav_total+dnav_total;
    dnav_waiting=max((cond-channels), 0)*Pcond;
    nav_waiting=nav_waiting+dnav_waiting;
    dnav_service=min(cond, channels)*Pcond;
    nav_service=nav_service+dnav_service;
  endfor
 
  nav_total
  sum(nav_total)
  nav_waiting
  sum(nav_waiting)
  nav_service
  sum(nav_service)

  global powers
  tav_total=(nav_total./nav_service)./powers
  tav_waiting=(nav_waiting./nav_service)./powers

  export_result(nav_total, nav_waiting, tav_total, tav_waiting);

  conditions
endfunction

main()
