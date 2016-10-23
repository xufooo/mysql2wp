# -*-coding:utf-8 -*-

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts,NewPost


wp = Client('http://xxxx/xmlrpc.php', 'xxxx', 'xxxx')
post = WordPressPost()
post.title = 'Test Title'
post.terms_names = {
	'category': ['Test Category'],
}
post.content = '<p>Test Contents' + \
			   '</p><img class="alignnone size-medium" src="xxx"' +\
			   ' />'

wp.call(NewPost(post))
