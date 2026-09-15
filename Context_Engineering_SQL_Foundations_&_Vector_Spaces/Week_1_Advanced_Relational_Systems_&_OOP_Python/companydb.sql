create table organization(
ORGANIZATION_ID int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
ORGANIZATION_NAME VARCHAR(100),
MAIL_ID VARCHAR(100) 
);


CREATE TABLE USERS(
USER_ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
ORGANIZATION_ID INT,
USERNAME VARCHAR(100),


FOREIGN KEY (ORGANIZATION_ID)
  references ORGANIZATION(organization_id)

);


CREATE TABLE ACTIVITY_LOGs(
ACTIVITY_ID bigint generated always as IDENTITY primary key,
USER_ID INT,
ACTIVITY VARCHAR(50)
 CHECK (ACTIVITY IN ('log-in','log-out','sign-in','sign-out','editing','posting')),
 ACTIVITY_TIMING  TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY (USER_ID)
references users(user_id)
);




----------------------------------------------------------------------------
insert into organization(ORGANIZATION_NAME,MAIL_ID)
select  
CASE 
WHEN random()<0.15 THEN 'XYZ'||gs
when random()<0.25 then 'PQR'||gs
when random()<0.5 then 'KLM'||gs
when random()<0.75 then 'FGH'||gs
else 'VIO'||gs
end as ORGANIZATION_NAME,

CASE 
when random()<0.25 then gs|| 'PQR'||'@gmail.com'
when random()<0.5 then gs|| 'LMN'||'@gmail.com'
when random()<0.75 then gs|| 'ABC'||'@gmail.com'
when random()<0.99 then gs|| 'TBD'||'@gmail.com'
else gs||'KOI'||'@gmail.com'
end as MAIL_ID

FROM generate_series(1000,1999) as gs;


select * from organization;
-----------------------------------------------------------------------------


insert into users(organization_id,username)
select 

floor(random()*1000+1)::int,

case 
when random()<0.25 then 'ASVDK_'||gs
when random()<0.50 then 'QWEOO_'||gs
when random()<0.70 then 'MQWOP_'||gs
when random()<0.99 then 'ZXRTA_'||gs
else 'PZWQM_'||gs
end as username 

from generate_series(10000,(40000-1)) as gs;

select * from users;



insert into activity_logs(user_id,activity,activity_timing)
select

floor(random()*30000+1)::int,

case  
when random()<0.15 then 'log-in'
when random()<0.30 then 'log-out'
when random()<0.50 then 'sign-in'
when random()<0.65 then 'sign-out'
when random()<0.85 then 'editing'
else  'posting'
end as activity,

CURRENT_TIMESTAMP - random()*interval'30 days'


from generate_series(100000,299999) as gs;


select * from activity_logs; 

