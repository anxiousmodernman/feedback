-- Show database pre-state
select b.briefid, b.brief_name, lsb.status, s.email, s.subscriberid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.email = 'changesubscriberptlyzs@smartbrief.com' --TODO change this to whatever user you are testing


-- Unsub All SQL query 1
select b.briefid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.subscriberid = $SUBSCRIBER_ID -- PHP variable for the subscriber you're editing
and b.parentid is null


-- Unsub All SQL query 2
select b.briefid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.subscriberid = $SUBSCRIBER_ID -- PHP variable for the subscriber you're editing
and b.parentid is not null


-- Unsub All SQL query 3
select distinct b.parentid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.subscriberid = $SUBSCRIBER_ID -- PHP variable for the subscriber you're editing
and b.parentid in ( select b1.parentid
                    from brief b1
                    where b1.briefid in (  $child_brief_unsub  ) -- PHP array built from query 2
                    )
and b.parentid not in (  select b2.briefid
                         from brief b2
                         where b2.briefid in (  $main_brief_unsub  ) -- PHP array built from query 1
                         )
                         

-- Unsub All SQL query 4
-- This deactivates marketing messages
update subscriber
set marketing_message = 0
where subscriberid = $SUBSCRIBER_ID


-- insert "U" row to UNSUBSCRIBE for each item necessary
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ( $SUBSCRIBER_ID, $BRIEF_ID, 'U', 'fromFeedback' )  -- must give correct briefids from 
                                                           -- $main_brief_unsub, $child_brief_unsub, $other_parent_brief_unsub


