alter table movie
add constraint uniqueLength unique(length);

alter table movie 
add constraint uniqueStudioAndLength unique(studioname, length);

alter table movie
drop constraint uniqueStudioAndLength,
constraint uniqueLength;
