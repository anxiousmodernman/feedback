results of 1
$giver_main
7325D171-85C1-4A99-9773-4FE6659490B5


results of 2
$giver_child
86DF6B24-D02F-4771-B862-B4DCFAE12FF7


results of 3
$giver_child_parent_unsub
391CAE11-B499-4878-B8D0-EFE59540D516


For each item in giver_child, add a U row

-- insert "U" row to UNSUBSCRIBE 
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ( '3FAC984C-D693-4E9D-8125-E004CD63A075', '86DF6B24-D02F-4771-B862-B4DCFAE12FF7', 'U', 'fromFeedback' )


For each item in giver_child_parent_unsub, add a U row
-- insert "U" row to UNSUBSCRIBE 
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ( '3FAC984C-D693-4E9D-8125-E004CD63A075', '391CAE11-B499-4878-B8D0-EFE59540D516', 'U', 'fromFeedback' )


insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ('3FAC984C-D693-4E9D-8125-E004CD63A075', '7325D171-85C1-4A99-9773-4FE6659490B5', 'U', 'fromFeedback')


results of 4
$receiver_child_unsub
40227BB1-F01D-4E1D-987D-6B5485EF6DC9
8346EB46-80FD-49F2-8738-90A4A4499A6D


-- insert "U" row to UNSUBSCRIBE 
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ( '74CF899E-6642-4DF0-8061-9D6FB4BDC3E4', '40227BB1-F01D-4E1D-987D-6B5485EF6DC9', 'U', 'fromFeedback' )


For each item in giver_child_parent_unsub, add a U row
-- insert "U" row to UNSUBSCRIBE 
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ( '74CF899E-6642-4DF0-8061-9D6FB4BDC3E4', '8346EB46-80FD-49F2-8738-90A4A4499A6D', 'U', 'fromFeedback' )



-- insert an "S" row to SUBSCRIBE
-- subscribe to AAAA
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ('74CF899E-6642-4DF0-8061-9D6FB4BDC3E4', '7325D171-85C1-4A99-9773-4FE6659490B5', 'S', 'fromFeedback')
insert into subscriber_brief_profile (subscriberid, briefid)
values ('74CF899E-6642-4DF0-8061-9D6FB4BDC3E4', '7325D171-85C1-4A99-9773-4FE6659490B5')

