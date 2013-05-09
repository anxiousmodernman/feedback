/*
 Subscriptions for 
 feedback-profileupdate@smartbrief.com
 
 subscriberid = 'DC2EB298-AE87-425F-9F24-F62393986815'
 */
 

-- subscribe to AAAA
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ('DC2EB298-AE87-425F-9F24-F62393986815', '7325D171-85C1-4A99-9773-4FE6659490B5', 'S', 'fromFeedback')
insert into subscriber_brief_profile (subscriberid, briefid)
values ('DC2EB298-AE87-425F-9F24-F62393986815', '7325D171-85C1-4A99-9773-4FE6659490B5')

-- subscribe to CIA
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ('DC2EB298-AE87-425F-9F24-F62393986815', '391CAE11-B499-4878-B8D0-EFE59540D516', 'S', 'fromFeedback')
insert into subscriber_brief_profile (subscriberid, briefid)
values ('DC2EB298-AE87-425F-9F24-F62393986815', '391CAE11-B499-4878-B8D0-EFE59540D516')

-- subscribe to CIA10/8/2007 (for trialbrief2)
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ('DC2EB298-AE87-425F-9F24-F62393986815', '86DF6B24-D02F-4771-B862-B4DCFAE12FF7', 'S', 'fromFeedback')
insert into subscriber_brief_profile (subscriberid, briefid)
values ('DC2EB298-AE87-425F-9F24-F62393986815', '86DF6B24-D02F-4771-B862-B4DCFAE12FF7')

-- subscribe to CIA4/6/2011_Foodies (for trialbrief2B)
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ('DC2EB298-AE87-425F-9F24-F62393986815', 'DC7F2575-4BFC-4597-BB50-EEB2E7C6DB2B', 'S', 'fromFeedback')
insert into subscriber_brief_profile (subscriberid, briefid)
values ('DC2EB298-AE87-425F-9F24-F62393986815', 'DC7F2575-4BFC-4597-BB50-EEB2E7C6DB2B')

-- subscribe to SOCIALMEDIA11/26/2008 (for trialbrief3)
insert into link_subscriber_brief (subscriberid, briefid, status, reason)
values ('DC2EB298-AE87-425F-9F24-F62393986815', '2B97B751-E853-4ED0-A694-E8DA13B809CC', 'S', 'fromFeedback')
insert into subscriber_brief_profile (subscriberid, briefid)
values ('DC2EB298-AE87-425F-9F24-F62393986815', '2B97B751-E853-4ED0-A694-E8DA13B809CC')

/* REQUIRED FOR TEST 6 and TEST ???

-- subscribe to SocialMedia (for parentbrief3)
insert into link_subscriber_brief (subscriberid, briefid, status, reason) 
values ('DC2EB298-AE87-425F-9F24-F62393986815', '9A6B83EA-211A-4D95-9BF3-DEC352898000', 'S', 'fromFeedback')
insert into subscriber_brief_profile (subscriberid, briefid)
values ('DC2EB298-AE87-425F-9F24-F62393986815', '9A6B83EA-211A-4D95-9BF3-DEC352898000')

*/
