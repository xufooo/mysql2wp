# -*-coding:utf-8 -*-

from datetime import datetime
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts,NewPost


wp = Client('http://xxxx/xmlrpc.php', 'xxxx', 'xxxx')
post = WordPressPost()
post.title = 'Test Title'
post.date = datetime.strptime('xxxx-xx-xx xx:xx:xx', '%Y-%m-%d %H:%M:%S')
post.terms_names = {
	'category': ['Uncategorized'],
}
post.content = '<p>Test Contents' + \
			   '</p><img src="xxx"' +\
			   ' />'
post.post_status = 'publish'

wp.call(NewPost(post))
