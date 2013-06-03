-- Show database pre-state 
select b.briefid, b.brief_name, lsb.status, s.email, s.subscriberid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.email = 'changesubscriberptlyzs@smartbrief.com' --TODO change this to whatever user you are testing


-- merge SQL query 1
select b.briefid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.subscriberid = $GIVER_SUBSCRIBER_ID -- PHP variable
and b.parentid is null


-- merge SQL query 2
select b.briefid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.subscriberid = $GIVER_SUBSCRIBER_ID -- PHP variable
and b.parentid is not null


-- merge SQL query 3
select distinct b.parentid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.subscriberid = $GIVER_SUBSCRIBER_ID -- PHP variable
and b.parentid is not null


-- insert "U" row to UNSUBSCRIBE 
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ( $SUBSCRIBER_ID, $BRIEF_ID, 'U', 'fromFeedback' )


-- merge SQL query 4
select distinct b.briefid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.subscriberid = $RECEIVER_SUBSCRIBER_ID -- PHP variable
and b.parentid in ('', '', '', '')  -- etc... TODO Unpack $giver_main array into a list of briefid with this sql syntax


-- insert an "S" row to SUBSCRIBE
-- subscribe to AAAA
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ($SUBSCRIBER_ID, $BRIEF_ID, 'S', 'fromFeedback')
insert into subscriber_brief_profile (subscriberid, briefid)
values ($SUBSCRIBER_ID, $BRIEF_ID)


