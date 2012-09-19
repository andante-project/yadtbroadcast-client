from pythonbuilder.core import use_plugin, init, Author

use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin('python.distutils')
use_plugin('python.pydev')

use_plugin('copy_resources')

default_task = 'publish'

version = '1.1.1'
summary = 'YADT - an Augmented Deployment Tool - The Broadcast Client Part'
description = """Yet Another Deployment Tool - The Broadcast Client Part
- sends state information to a Yadt Broadcast Server instance
- sends information on start/stop/status/update
"""
authors = [Author('Arne Hilmann', 'arne.hilmann@gmail.com')]
url     = 'http://github.com/yadt/yadtbroadcast-client'
license = 'GNU GPL v3'

@init
def set_properties (project):
    project.depends_on('Twisted')
    project.depends_on('autobahn')
    
    project.set_property('coverage_break_build', False)
    project.set_property('pychecker_break_build', False)

    project.get_property('distutils_commands').append('bdist_rpm')    
    project.set_property('copy_resources_target', '$dir_dist')
    project.get_property('copy_resources_glob').append('setup.cfg')
    project.set_property('dir_dist_scripts', 'scripts')

    project.set_property('distutils_classifiers', [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Topic :: System :: Networking',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration'
    ])

