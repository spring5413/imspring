/**
 * author:spring
 * title:
 * ctime:15/7/1
 * */

module("core", {
    setup: function() {
        // 在每个测试之前运行
    },
    teardown: function() {
        // 在每个测试之后运行
    }
});

test("测试除法",function(){
    equal(devide(1,0),"error");
    equal(devide(),"not_a");
    ok(devide("aa",12),"a_NaN");
    ok(devide(12,"bb"),"b_NaN");
});

QUnit.test( "测试除法2", function( assert ) {
    assert.equal( devide(1,0), "error", "除数为0" );
    assert.equal(devide(),"not_a","分子没填");
    assert.equal(devide("aa",12),"a_NaN","分子不是数字");
    assert.equal(devide(12,"bb"),"b_NaN","分母不是数字");
});