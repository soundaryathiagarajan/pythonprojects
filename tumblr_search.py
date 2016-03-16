import pytumblr

import simplejson
client = pytumblr.TumblrRestClient(
				'',
				'',
				'',
				'',
				)
def dumpJSON(res,fname='/tmp/test.dmp'):
	f = open(fname,'w')
	simplejson.dump(res,f)
	f.close()
	print "Saved in %s"%fname


def getPosts(q):
	before_param=None
	result = []
	while True:
		if not before_param:		
			posts = client.tagged(q)
		else:
			posts = client.tagged(q,filter='text',before=before_param)
		if not posts:
			print "No posts available"
			break
		for post in posts:
			if post['type'] == 'text':
				post['matched_names'] = [q]
				result.append(post)
		if len(result)>=100:
			break
		before_param = posts[-1]['timestamp']
		print 'Fetched %d posts for %s'%(len(result),q)
	return result

	
if __name__ == '__main__':
	qs = ['Hillary Clinton', 'Bernie Sanders', 'Jeb Bush', 'Donald Trump', 'John Kasich', 'Marco Rubio', 'Scott Walker']
	for each in qs:
		fname = 'tumblr_data/' + each.replace(' ','_')+'.dmp'
		print 'Getting posts for %s'%each
		posts = getPosts(each)
		print "Got %d posts"%len(posts)
		dumpJSON(posts,fname)
		







