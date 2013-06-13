-- Show database pre-state
select b.briefid, b.brief_name, lsb.status, s.email, s.subscriberid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.email = 'changesubscriberptlyzs@smartbrief.com' --TODO change this to whatever user you are testing


-- Unsub One SQL query 1
-- If this returns null, then the subscriber is already unsubscribed
select b.briefid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.subscriberid = $SUBSCRIBER_ID -- PHP variable for the subscriber you're editing
and b.briefid = $PASSED_IN_BRIEFID  -- passed in


-- Unsub One SQL query 2
-- This query gets the parent, if a parent subscription exists
select b.parentid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.subscriberid = $SUBSCRIBER_ID -- PHP variable for the subscriber you're editing
and b.briefid = $PASSED_IN_BRIEFID  -- passed in


-- Unsub One SQL query 3
-- This query gets children, if subscriptions to children exist
select distinct b.briefid
from link_subscriber_brief lsb
inner join brief b on lsb.briefid = b.briefid
inner join subscriber s on lsb.subscriberid = s.subscriberid
inner join current_subscriptions cs on cs.subscriberid = s.subscriberid and cs.briefid = lsb.briefid
where s.subscriberid = $SUBSCRIBER_ID -- PHP variable for the subscriber you're editing
and b.parentid = $PASSED_IN_BRIEFID  -- passed in; this should exclude anything in $unsub_array_1


-- insert "U" row to UNSUBSCRIBE for each item necessary
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ( $SUBSCRIBER_ID, $BRIEF_ID, 'U', 'fromFeedback' )  -- must give correct briefids from 
                                                           -- $unsub_array_1, $parent_unsub_array, $unsub_array_2


