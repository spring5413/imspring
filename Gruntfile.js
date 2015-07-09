// 包装函数
module.exports = function(grunt) {

    // LiveReload的默认端口号，你也可以改成你想要的端口号
    var lrPort = 35729;
    // 使用connect-livereload模块，生成一个与LiveReload脚本
    // &lt;script src=&quot;http://127.0.0.1:35729/livereload.js?snipver=1&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;
    var lrSnippet = require('connect-livereload')({ port: lrPort });
    // 使用 middleware(中间件)，就必须关闭 LiveReload 的浏览器插件
    var lrMiddleware = function(connect, options) {
        return [
            // 把脚本，注入到静态文件中
            lrSnippet,
            // 静态文件服务器的路径
            connect.static(options.base[0]),
            // 启用目录浏览(相当于IIS中的目录浏览)
            connect.directory(options.base[0])
        ];
    };

  // 任务配置,所有插件的配置信息
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    // uglify插件的配置信息
    uglify: {
        options: {
          banner: '/*! This is uglify test - ' +
            '<%= grunt.template.today("yyyy-mm-dd") %> */',
          beautify: true,//是否压缩
          mangle: false, //不混淆变量名
          compress:true,//打开或关闭使用默认选项源压缩。
        },
        app_task: {
          files: {
            'build/app.min.js': ['lib/index.js', 'lib/test.js']
          }
        }
    },
    // watch插件的配置信息
    watch: {
        another: {
            files: ['lib/*.js'],
            tasks: ['uglify'],
            options: {
                // Start another live reload server on port 1337
                livereload: lrPort
            },
            files: ['*.html', 'css/*', 'js/*', 'images/**/*']
        }
    },
    connect: {
        options: {
            port: 8000,
            base: '.',
            hostname: 'localhost'
        },
        livereload: {
            options: {
                // 通过LiveReload脚本，让页面重新加载。
                middleware: lrMiddleware
            }
        }
    },
      qunit: {
        all: {
          options: {
            urls: [
              'http://localhost:8000/test/foo.html'
            ]
          }
        }
      }
  });

  // 告诉grunt我们将使用插件
  grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-connect');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-qunit');

  // 告诉grunt当我们在终端中输入grunt时需要做些什么
  grunt.registerTask('default', ['uglify','connect','watch','qunit']);
  grunt.registerTask('test', ['connect','qunit']);

    grunt.event.on('qunit.spawn', function (url) {
      grunt.log.ok("Running test: " + url);
    });

};