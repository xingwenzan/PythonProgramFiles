import random
import time

import requests
from lxml import etree



def getURL(param):


  url = f"https://gaokao.chsi.com.cn/sch/search--ss-on,option-qg,searchType-1,start-{param}.dhtml"

  payload={}
  headers = {
    'Cookie': 'CHSICC01=!h5qjKVh0xSsplurzYxYLahOzddj6Y3g9hQmh37VqpXbWWuNfquWgLtzJ1X4KJ2Nkw+OxmmIdsiYCig==; JSESSIONID=597FB73E3B03B8B20D17D2F76ACBC981; XSRF-CCKTOKEN=56ac37dffc7697b70aef33c92dab87f4'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)


  if response.status_code ==200:
    print("爬到了"+str(param))


for i in range(1,139):
  getURL(20*(i-1))


time.sleep(random.randint(3,10))

htmlCONTONT = '''

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">
    <title>院校信息库_阳光高考</title>
    <meta name="keywords" content="高校名单,教育部直属高校,中央部委所属高校,本科高校,高职专科,有研究生院,独立学院,民办高校" />
    <meta name="description" content="提供最权威的高校查询，可以按照院校所在地、主管部门类别、办学类型、学历层次等查询。也可根据院校分类直接查看相应类型高校名单。" />
    <link rel="stylesheet" href='https://t1.chei.com.cn/common/plugins/autocomplete/jquery.autocomplete.css'/>
    


<link rel="dns-prefetch" href="//axvert.chsi.com.cn">
<link rel="dns-prefetch" href="//t1.chei.com.cn">
<link rel="dns-prefetch" href="//t2.chei.com.cn">
<link rel="dns-prefetch" href="//t3.chei.com.cn">
<link rel="dns-prefetch" href="//t4.chei.com.cn">
<link rel="dns-prefetch" href="//www.google-analytics.com">
<link rel="stylesheet" href="https://t1.chei.com.cn/common/ch/iconfont.css">
<link rel="stylesheet" href="https://t1.chei.com.cn/common/css/share.css"/>
<link rel="stylesheet" href="https://t3.chei.com.cn/gaokao/assets/src/css/gaokao.min.css?20180124">
<!--<link rel="stylesheet" href="/assets/src/css/gaokao.min.css">-->
<script src="https://t1.chei.com.cn/common/jquery/1.8.3/jquery.min.js"></script>
<script src="https://t1.chei.com.cn/common/axvert/js/showchsi_m.js"></script>
<script src="https://t1.chei.com.cn/common/js/snsshare.js"></script>
<script src="https://t1.chei.com.cn/common/js/goToTop.js"></script>
<!--[if IE 6]>
<script src="https://t4.chei.com.cn/gaokao/js/IE6PNG.js"></script>
<script>DD_belatedPNG.fix('#dhBG,#dh_logo,img');</script>
<![endif]-->
    

<script src="https://t1.chei.com.cn/common/zhuge/zhuge-1.0.0.js"></script>
<script>
    function zhugeInit(autoTrack) {
        window.zhuge.load('a5f21d6abc554e3c9e4c17aade025fd8', {
            autoTrack: autoTrack
        });
    }
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-100524-6"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'UA-100524-6');
</script>


</head>

<body class="ch-sticky">
<img style="display: block;" src='//t1.chei.com.cn/common/wap/images/share_gk.jpg' width='0' height='0'/>
<div class="main-wrapper">
    






<style>
    /**
     * description: 吊顶;
     * author: myx;
     * date: 2017-12;
     */
    .top-nav-wrapper {
        width: 100%;
        height: 38px;
        line-height: 42px;
        background: #f5f5f5;
        border-bottom: 1px solid #d6d6d6;
        font-size: 12px;
        overflow: hidden;
    }

    .top-nav-wrapper a {
        color: #333;
    }

    .top-nav-wrapper a.hot {
        color: #ee6464;
    }

    .top-nav-wrapper a:hover {
        text-decoration: underline;
    }

    .top-nav-wrapper .top-nav {
        width: 1180px;
        margin: 0 auto;
    }

    .top-nav-wrapper .top-nav-list {
        float: left;
        width: 980px;
        height: 38px;
    }

    .top-nav-wrapper .top-nav-list a {
        margin: 0 10px;
    }

    .top-nav-wrapper .top-nav-list a.top-nav-home {
        display: inline-block;
        width: 75px;
        height: 38px;
        margin-right: 15px;
        margin-left: 0px;
        margin-top: -1px;
        background-image: url("https://t2.chei.com.cn/gaokao/assets/src/images/logo.png");
        background-image: -webkit-image-set(url("https://t2.chei.com.cn/gaokao/assets/src/images/logo.png") 1x, url("https://t2.chei.com.cn/gaokao/assets/src/images/logo2x.png") 2x);
        background-repeat: no-repeat;
        background-position: 0 0px;
        color: #1db278;
        font-weight: bold;
        vertical-align: middle;
    }

    .top-nav-wrapper .top-nav-list a.top-nav-home:hover {
        text-decoration: none;
    }

    .top-nav-wrapper .top-nav-load {
        float: right;
        width: 160px;
        height: 38px;
        text-align: right;
    }

    .top-nav-wrapper .top-nav-load a {
        margin: 0 5px;
    }

    .top-nav-wrapper a.username {
        color: #1db278;
        width: 100px;
		overflow: hidden;
		text-overflow: ellipsis;
        float: left;
    }
</style>
<div class="top-nav-wrapper">
    <div class="top-nav clearfix">
        <div class="top-nav-list">
            <a href="/" class="top-nav-home">&ensp;</a>
            <a href="/">首页</a>
            <a href="/zsgs/mdgs.jsp">名单公示</a>
            <a href="/zsgs/zhangcheng/">招生章程</a>
            <a href="/sch/">院校库</a>
            <a href="/zyk/pub/myd/schAppraisalTop.action">院校满意度</a>
            <a href="/zyk/pub/myd/specAppraisalTop.action">专业满意度</a>
            <a href="/zyk/pub/zytj/recommendTop.action">专业推荐</a>
            <a href="/zyk/zybk/">专业知识库</a>
            <a href="/zyk/zybk/zyjd/listPage/">专业解读</a>
            <a href="/zxdy/">咨询周</a>
            <a href="/zxdy/zxs--method-listDefault,forumid-6267733,year-2007,start-0.dhtml">咨询室</a>
            <a href="/zyck/" target="_blank">高考填报志愿参考</a>
        </div>
        <div class="top-nav-load clearfix">
            






    <a href="/user/userAccountLogin.do?entrytype=gkstu">登录</a>
        |
    <a href="https://account.chsi.com.cn/account/account!newaccount?from=gaokao-zixun">注册</a>

        </div>
    </div>
</div> 
    <!--头部区域-->
    <div class="header-wrapper ch-simple">
        <div class="ch-header-second clearfix">
            <h1>院校库</h1>
        </div>
    </div>
    <!--主体区域-->
    <div class="container">
        






<style>
    .sch-tab {
        height: 39px;
        margin-top: 10px;
        margin-bottom: 6px;
        border-color: #eaeaea;
    }

    .sch-tab .tab-item {
        border-width: 3px;
        margin-right: 20px;
    }

    .sch-tab .tab-item a {
        padding-left: 0;
        padding-right: 0;
    }

    .yxk-filter {
        padding: 0;
        border: none;
        margin-bottom: 8px;
        margin-top: 24px;
    }

    .yxk-filter li {
        padding: 4px 0;
    }

    .yxk-filter li.search-bar {
        margin-bottom: 5px;
    }

    .yxk-filter .list-th {
        width: 105px;
        padding-right: 0;
        text-align: left;
        font-weight: 700;
        font-size: 14px;
    }

    .yxk-filter li.yxk-option-con .list-td {
        width: 1075px;
        padding-left: 0;
    }

    .yxk-fliter-list .ch-input {
        width: 430px;
        border-radius: 4px;
    }

    .yxk-fliter-list .ch-btn {
        border-radius: 4px;
    }

    .yxk-fliter-list .ch-select {
        border-radius: 4px;
    }

    .yxk-filter .yxk-option {
        padding: 0;
        margin-right: 20px;
    }

    .yxk-filter .yxk-option.selected {
        color: #1db278;
        background: none;
    }

    .yxk-filter .ch-check-label {
        padding-left: 0;
    }

    .yxk-filter .ch-check-label + .ch-check-label {
        margin-left: 10px;
    }

    .yxk-filter .yxk-xz a {
        margin-right: 10px;
    }

    .yxk-filter .ch-check-label input[type=checkbox] {
        position: relative;
        top: -1px;
    }
</style>
<form class="zx-search-yx" action="/sch/search.do" name="form1" id="form1">


    <div class="yxk-filter">
        <ul class="yxk-fliter-list">
            <li class="yxk-option-con search-bar clearfix">
                <div class="clearfix">
                    <input class="ch-hide" name="searchType" value="1" type="hidden"/>
                    <div class="item-inline js-yxmc ">
                        <input class="ch-input" style="margin-left: 0;" type="text" maxlength="50" name="yxmc" id="yxmc"
                               placeholder="请输入院校名称"/>
                    </div>

                    <div class="item-inline">
                        <input class="ch-btn ch-btn-big" type="submit" value="查询"/>
                    </div>
                </div>
                <div style="color: #999999;margin-top: 5px;">（ 注：本名单未包含港澳台地区高等学校 ）</div>
            </li>
            <li class="yxk-option-con clearfix">
                <div class="list-th">院校所在地</div>
                <div class="list-td clearfix">
                    <select class="ch-hide" name="ssdm" id="ssdm">
                        <option value="">院校所在地</option>
                        
                            <option value="11"
                                    >
                                北京
                            </option>
                        
                            <option value="12"
                                    >
                                天津
                            </option>
                        
                            <option value="13"
                                    >
                                河北
                            </option>
                        
                            <option value="14"
                                    >
                                山西
                            </option>
                        
                            <option value="15"
                                    >
                                内蒙古
                            </option>
                        
                            <option value="21"
                                    >
                                辽宁
                            </option>
                        
                            <option value="22"
                                    >
                                吉林
                            </option>
                        
                            <option value="23"
                                    >
                                黑龙江
                            </option>
                        
                            <option value="31"
                                    >
                                上海
                            </option>
                        
                            <option value="32"
                                    >
                                江苏
                            </option>
                        
                            <option value="33"
                                    >
                                浙江
                            </option>
                        
                            <option value="34"
                                    >
                                安徽
                            </option>
                        
                            <option value="35"
                                    >
                                福建
                            </option>
                        
                            <option value="36"
                                    >
                                江西
                            </option>
                        
                            <option value="37"
                                    >
                                山东
                            </option>
                        
                            <option value="41"
                                    >
                                河南
                            </option>
                        
                            <option value="42"
                                    >
                                湖北
                            </option>
                        
                            <option value="43"
                                    >
                                湖南
                            </option>
                        
                            <option value="44"
                                    >
                                广东
                            </option>
                        
                            <option value="45"
                                    >
                                广西
                            </option>
                        
                            <option value="46"
                                    >
                                海南
                            </option>
                        
                            <option value="50"
                                    >
                                重庆
                            </option>
                        
                            <option value="51"
                                    >
                                四川
                            </option>
                        
                            <option value="52"
                                    >
                                贵州
                            </option>
                        
                            <option value="53"
                                    >
                                云南
                            </option>
                        
                            <option value="54"
                                    >
                                西藏
                            </option>
                        
                            <option value="61"
                                    >
                                陕西
                            </option>
                        
                            <option value="62"
                                    >
                                甘肃
                            </option>
                        
                            <option value="63"
                                    >
                                青海
                            </option>
                        
                            <option value="64"
                                    >
                                宁夏
                            </option>
                        
                            <option value="65"
                                    >
                                新疆
                            </option>
                        
                    </select>
                    <span class="yxk-option js-option selected" data-id="">全部</span>
                    
                        <span class="yxk-option js-option "
                              data-id="11">北京</span>
                    
                        <span class="yxk-option js-option "
                              data-id="12">天津</span>
                    
                        <span class="yxk-option js-option "
                              data-id="13">河北</span>
                    
                        <span class="yxk-option js-option "
                              data-id="14">山西</span>
                    
                        <span class="yxk-option js-option "
                              data-id="15">内蒙古</span>
                    
                        <span class="yxk-option js-option "
                              data-id="21">辽宁</span>
                    
                        <span class="yxk-option js-option "
                              data-id="22">吉林</span>
                    
                        <span class="yxk-option js-option "
                              data-id="23">黑龙江</span>
                    
                        <span class="yxk-option js-option "
                              data-id="31">上海</span>
                    
                        <span class="yxk-option js-option "
                              data-id="32">江苏</span>
                    
                        <span class="yxk-option js-option "
                              data-id="33">浙江</span>
                    
                        <span class="yxk-option js-option "
                              data-id="34">安徽</span>
                    
                        <span class="yxk-option js-option "
                              data-id="35">福建</span>
                    
                        <span class="yxk-option js-option "
                              data-id="36">江西</span>
                    
                        <span class="yxk-option js-option "
                              data-id="37">山东</span>
                    
                        <span class="yxk-option js-option "
                              data-id="41">河南</span>
                    
                        <span class="yxk-option js-option "
                              data-id="42">湖北</span>
                    
                        <span class="yxk-option js-option "
                              data-id="43">湖南</span>
                    
                        <span class="yxk-option js-option "
                              data-id="44">广东</span>
                    
                        <span class="yxk-option js-option "
                              data-id="45">广西</span>
                    
                        <span class="yxk-option js-option "
                              data-id="46">海南</span>
                    
                        <span class="yxk-option js-option "
                              data-id="50">重庆</span>
                    
                        <span class="yxk-option js-option "
                              data-id="51">四川</span>
                    
                        <span class="yxk-option js-option "
                              data-id="52">贵州</span>
                    
                        <span class="yxk-option js-option "
                              data-id="53">云南</span>
                    
                        <span class="yxk-option js-option "
                              data-id="54">西藏</span>
                    
                        <span class="yxk-option js-option "
                              data-id="61">陕西</span>
                    
                        <span class="yxk-option js-option "
                              data-id="62">甘肃</span>
                    
                        <span class="yxk-option js-option "
                              data-id="63">青海</span>
                    
                        <span class="yxk-option js-option "
                              data-id="64">宁夏</span>
                    
                        <span class="yxk-option js-option "
                              data-id="65">新疆</span>
                    
                </div>
            </li>
            <li class="yxk-option-con clearfix">
                <div class="list-th">主管部门类别</div>
                <div class="list-td clearfix">
                    <select class="ch-hide" name="yxls">
                        <option value="" selected='selected'>全部</option>
                        <option value="moe" >教育部</option>
                        <option value="min" >其他部委</option>
                        <option value="loc" >地方</option>
                        <option value="army" >军校</option>
                    </select>
                    <span class="yxk-option js-option js-ls selected"
                          data-id="">全部</span>
                    <span class="yxk-option js-option "
                          data-id="moe">教育部</span>
                    <span class="yxk-option js-option "
                          data-id="min">其他部委</span>
                    <span class="yxk-option js-option "
                          data-id="loc">地方</span>
                    <span class="yxk-option js-option "
                          data-id="army">军校</span>
                </div>
            </li>
            <li class="yxk-option-con clearfix">
                <div class="list-th">学历层次</div>
                <div class="list-td clearfix">
                    <select class="ch-hide" name="xlcc">
                        <option value="" selected='selected'>全部</option>
                        <option value="bk" >本科</option>
                        <option value="gzzk" >高职(专科)</option>
                    </select>
                    <span class="yxk-option js-option js-ls selected"
                          data-id="">全部</span>
                    <span class="yxk-option js-option " data-id="bk">本科</span>
                    <span class="yxk-option js-option "
                          data-id="gzzk">高职(专科)</span>
                </div>
            </li>
            <li class="yxk-xz clearfix">
                <div class="list-th">院校特性</div>
                <div class="list-td">
                    <label class="ch-check-label ">
                        <input type="checkbox" name="zgsx" id="ylxx" value="ylxx"
                                />一流大学建设高校
                    </label>
                    <label class="ch-check-label ">
                        <input type="checkbox" name="zgsx" id="ylxk" value="ylxk"
                                />一流学科建设高校
                    </label>

                    <label class="ch-check-label ">
                        <input type="checkbox" name="zgsx" id="yjsy" value="yjsy"
                                />研究生院
                    </label>
                    <a href="//yz.chsi.com.cn/kyzx/kp/201101/20110119/161300374.html" target="_blank"><i
                            class="iconfont" title="研究生院">&#xe67b;</i></a>
                    <label class="ch-check-label ">
                        <input type="radio" name="yxjbz" id="yxjbz" value="2"
                                />民办高校
                    </label>
                    <a href="//gaokao.chsi.com.cn/gkxx/gkcs/201712/20171212/1644084026.html" target="_blank"><i
                            class="iconfont" title="民办高校">&#xe67b;</i></a>
                    <label class="ch-check-label ">
                        <input type="radio" name="yxjbz" id="yxjbz" value="3"
                                />独立学院
                    </label>
                    <a href="//gaokao.chsi.com.cn/gkxx/zcdh/200803/20080307/3975622.html" target="_blank"><i
                            class="iconfont" title="独立学院">&#xe67b;</i></a>
                    <label class="ch-check-label ">
                        <input type="radio" name="yxjbz" id="yxjbz" value="4"
                                />中外合作办学
                    </label>
                    <label class="ch-check-label ">
                        <input type="radio" name="yxjbz" id="yxjbz" value="5"
                                />内地与港澳台地区合作办学
                    </label>
                </div>
            </li>
        </ul>
    </div>
</form>
<script src="https://t1.chei.com.cn/common/plugins/autocomplete/jquery.autocomplete.js"></script>
<script>
    function ischinese(str) {
        if (/[^\x00-\xff]/g.test(str)) {
            return true;
        } else {
            return false;
        }
    }

    function checkSpecial(str) {
        var reg = /^[^@\/\'\\\"#$%&\^\*]+$/;
        if (reg.test(str)) {
            return true;
        } else {
            return false;//包含非法字符
        }
    }

    function testZymc() {
        if ($('#zymc').is(':visible')) {
            var $this = $('#zymc'),
                $thisTrimVal = $.trim($this.val());
            if ($thisTrimVal.length < 2 || !ischinese($thisTrimVal)) {
                alert("专业名称请输入至少2个汉字");
                return false;
            } else if ($('#sySsdm').val() == '') {
                alert("请选择考生所在地");
                return false;
            } else if ($thisTrimVal.length > 50) {
                alert("输入文字不能超过50个汉字");
                return false;
            } else if (!checkSpecial($thisTrimVal) && $thisTrimVal.length != '') {
                alert("不能包含特殊字符");
                return false;
            } else {
                return true;
            }
        } else {
            return true;
        }
    }

    $(function () {
        $("#yxmc").val('');
        $("#zymc").val('');
        $('.tab-item').click(function () {
            var $this = $(this);
            $this.addClass('selected').siblings('.tab-item').removeClass('selected');
            $this.find('input[name=searchType]').prop('checked', true);
            $this.siblings('.tab-item').find('input[name=searchType]').prop('checked', false);
            if ($this.find('input[name=searchType]').val() == 2) {
                $('.js-zymc').removeClass('ch-hide');
                $('.yxk-filter .red').removeClass('ch-hide');
                $('.yxk-filter select[name=sySsdm]').removeClass('ch-hide');
                $('.js-yxmc').addClass('ch-hide');
                $('#yxmc').val('');
            } else {
                $('.js-zymc').addClass('ch-hide')
                $('#zymc').val('');
                $('.yxk-filter .red').addClass('ch-hide');
                $('.yxk-filter select[name=sySsdm]').addClass('ch-hide');
                $('.js-yxmc').removeClass('ch-hide');
            }
        })
        //自动完成
        $("#yxmc").autocomplete('/sch/info/auto.jsp', {
            extraParams: {
                type: 'yxk_yx'
            },
            selectFirst: true,
            autoFill: true,
            selectOnly: true,
            remoteDataType: 'json'
        });
        $("#zymc").autocomplete('/sch/info/auto.jsp', {
            extraParams: {
                type: 'zsjh_zy'
            },
            selectFirst: true,
            autoFill: true,
            selectOnly: true,
            remoteDataType: 'json'
        });
        //select模拟单选功能
        $('.js-option').click(function () {
            if (!testZymc()) {
                return false
            }
            var $this = $(this),
                thisVal = $(this).attr('data-id');
            if ($this.hasClass('selected')) {
                return;
            }
            $this.siblings('select').find('option').removeAttr('selected');
            $this.siblings('select').find('option[value=' + thisVal + ']').prop('selected', true);
            $this.addClass('selected').siblings().removeClass('selected');
            $('#form1').submit();
        });
        //复选框选择后提交表单
        $('.yxk-xz input[type=checkbox]').click(function () {
            if (!testZymc()) {
                return false
            }
            if ($(this).prop('checked')) {
                $(this).parents('label').addClass('selected');
            } else {
                $(this).parents('label').removeClass('selected');
            }
            $('#form1').submit();
        });
        //单选框选择后提交表单
        $('.yxk-xz input[type=radio]').each(function () {
            if ($(this).is(':checked')) {
                $(this).data('waschecked', true);
            } else {
                $(this).data('waschecked', false);
            }
        })
        $('.yxk-xz input[type=radio]').click(function () {
            if (!testZymc()) {
                return false
            }
            var domName = $(this).attr('name');
            var $radio = $(this);
            if ($radio.data('waschecked') == true) {
                $radio.prop('checked', false);
                $("input:radio[name='" + domName + "']").data('waschecked', false);
                $(this).parents('label').removeClass('selected');
            } else {
                $radio.prop('checked', true);
                $("input:radio[name='" + domName + "']").data('waschecked', false);
                $radio.data('waschecked', true);
                $(this).parents('label').addClass('selected');
            }
            $('#form1').submit();
        });
        $('#form1').submit(function () {
            var returnVal = true;
            $('#form1 input[type=text]').each(function () {
                var $this = $(this),
                    $thisTrimVal = $.trim($this.val());
                $this.val($thisTrimVal);
                if ($this.is(':visible')) {
                    if ($thisTrimVal.length > 50) {
                        alert("输入文字不能超过50个汉字");
                        returnVal = false;
                    } else if (!checkSpecial($thisTrimVal) && $thisTrimVal.length != '') {
                        alert("不能包含特殊字符");
                        returnVal = false;
                    } else if (!ischinese($thisTrimVal) && $thisTrimVal.length != '') {
                        alert("请确保输入汉字");
                        returnVal = false;
                    } else if ($this.attr('name') == 'zymc') {
                        if ($thisTrimVal.length < 2) {
                            alert("请输入至少2个汉字");
                            returnVal = false;
                        } else if ($('#sySsdm').val() == '') {
                            alert("请选择考生所在地");
                            returnVal = false;
                        }
                    } else {
                        $('select[name=sySsdm]').val('');
                    }
                }
            });
            return returnVal;
        });
    });
</script>
        






















<div class="yxk-table">
    <table class="ch-table">
        <tr>
            <th>院校名称</th>
            <th width="90">院校所在地</th>
            <th width="210">教育行政主管部门</th>
            <th width="120">学历层次</th>
            <th width="70" class="ch-table-center" style="line-height:20px;font-size: 14px;">一流大学<br>建设高校</th>
            <th width="70" class="ch-table-center" style="line-height:20px;font-size: 14px;">一流学科<br>建设高校</th>
            <th width="70" class="ch-table-center">研究生院</th>
            <th width="70" class="ch-table-center">满意度</th>
        </tr>
        
            
            
                
            
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-1.dhtml">
                                北京大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        教育部
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617187">4.7</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-2.dhtml">
                                中国人民大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        教育部
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617188">4.7</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-3.dhtml">
                                清华大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        教育部
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617189">4.8</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-4.dhtml">
                                北京交通大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        教育部
                    </td>
                    <td>
                        
                        
                        本科/高职(专科)
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>

                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617190">4.4</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-5.dhtml">
                                北京工业大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        北京市教育委员会
                    </td>
                    <td>
                        
                        
                        本科/高职(专科)
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>

                    <td class="ch-table-center">
                        
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617191">4.4</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-6.dhtml">
                                北京航空航天大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        工业和信息化部
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617192">4.4</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-7.dhtml">
                                北京理工大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        工业和信息化部
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617193">4.5</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-8.dhtml">
                                北京科技大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        教育部
                    </td>
                    <td>
                        
                        
                        本科/高职(专科)
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>

                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617194">4.5</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-9.dhtml">
                                北方工业大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        北京市教育委员会
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617195">4.5</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-10.dhtml">
                                北京化工大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        教育部
                    </td>
                    <td>
                        
                        
                        本科/高职(专科)
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>

                    <td class="ch-table-center">
                        
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617196">4.0</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-11.dhtml">
                                北京工商大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        北京市教育委员会
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617197">4.2</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-12.dhtml">
                                北京服装学院
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        北京市教育委员会
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617198">4.2</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-13.dhtml">
                                北京邮电大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        教育部
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>

                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617199">4.3</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-14.dhtml">
                                北京印刷学院
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        北京市教育委员会
                    </td>
                    <td>
                        
                        
                        本科/高职(专科)
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617200">4.2</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-15.dhtml">
                                北京建筑大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        北京市教育委员会
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617201">4.2</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-16.dhtml">
                                北京石油化工学院
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        北京市教育委员会
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617202">3.7</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-17.dhtml">
                                北京电子科技学院
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        中共中央办公厅
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617203">4.5</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-18.dhtml">
                                中国农业大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        教育部
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617204">4.7</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-19.dhtml">
                                北京农学院
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        北京市教育委员会
                    </td>
                    <td>
                        
                        
                        本科/高职(专科)
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>

                    <td class="ch-table-center">
                        
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617205">3.9</a>
                        
                    </td>
                </tr>
            
                <tr>
                    <td class="js-yxk-yxmc">
                        
                            <a target="_blank" href="/sch/schoolInfo--schId-20.dhtml">
                                北京林业大学
                            </a>
                        
                        
                    </td>
                    <td>
                        北京
                    </td>
                    <td>
                        教育部
                    </td>
                    <td>
                        本科
                        
                        
                        
                    </td>
                    <td class="ch-table-center">
                        
                    </td>
                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>

                    <td class="ch-table-center">
                        <i class="iconfont ch-table-tick">&#xe664;</i>
                    </td>
                    <!--todo 院校满意度-->
                    <td class="ch-table-center ch-table-link">
                        
                        
                            <a class="js-alert-myd" href="###" data-id="99617206">4.4</a>
                        
                    </td>
                </tr>
            
        
        
    </table>
    <div class="ch-page-wrapper clearfix">
        
	
	
	
	


	
	


<div class="pager-box clearfix">
<form method="post" name="PageForm" class="pageForm" id="PageForm" onsubmit="return gotopage(this);">
<ul class="ch-page clearfix">
	   
        <li class="lip unable"><span class="p-padding"><i class="iconfont"></i></span></li>
        
        <li class="lip selected"><a href="###">1</a></li>
        
        <li class="lip "><a href="https://gaokao.chsi.com.cn/sch/search--ss-on,option-qg,searchType-1,start-20.dhtml">2</a></li>
        
        <li class="lip "><a href="https://gaokao.chsi.com.cn/sch/search--ss-on,option-qg,searchType-1,start-40.dhtml">3</a></li>
        
        <li class="lip "><a href="https://gaokao.chsi.com.cn/sch/search--ss-on,option-qg,searchType-1,start-60.dhtml">4</a></li>
        
        <li class="lip "><a href="https://gaokao.chsi.com.cn/sch/search--ss-on,option-qg,searchType-1,start-80.dhtml">5</a></li>
        
       <li class="lip dot">...</li>
    
        <li class="lip"><a href="https://gaokao.chsi.com.cn/sch/search--ss-on,option-qg,searchType-1,start-2740.dhtml">138</a></li>
        
        <li class="lip"><a href="https://gaokao.chsi.com.cn/sch/search--ss-on,option-qg,searchType-1,start-20.dhtml"><i class="iconfont"></i></a></li>
        
    
    <li class="lip lip-input-box clearfix lip-last">
        <input type="text" class="page-input" value="1" name="page"/>
        <input type="submit" value="Go" class='page-btn' />
    </li>
    
 </ul> 

</form>
</div>
<script type="text/javascript">
<!--
function gotopage(obj){
    var PN = obj.page.value;
    var Num = parseInt(PN);
    if(isNaN(Num)){
        window.alert("请输入有效的数字");
        return false;
    }
    if (Num > 138) {
        window.alert("没有那么多页");
        return false;
    }
    if (Num < 1) {
        window.alert("请输入有效的数字");
        return false;
    }
    pagenum = (Num - 1) * 20;
    var actionStr = "https://gaokao.chsi.com.cn/sch/search--ss-on,option-qg,searchType-1,start-0.dhtml";
    actionStr = actionStr.replace(/start-\d+/, "start-" + pagenum);
    obj.action= actionStr;
    return true;
    }
//-->
</script>	
    </div>
</div>
<script>
	zhugeInit(false);
	zhuge.track('page-load',{
		'来源': 'PC',
		'页面名称': '院校库首页'
	})
</script>
    </div>
</div>
<!--底部区域-->


<!-- 4: 底部区域 -->
<style>
    /**
     * description: footer 共用底部;
     * author:myx;
     * date:2017-12;
     */

    .footer-wrapper {
        line-height: 30px;
        background: #282828;
        color: #ababab;
    }

    .footer-wrapper a {
        color: #ababab;
    }

    .footer-wrapper .footer {
        position: relative;
        width: 1180px;
        height: 198px;
        margin: 0 auto;
    }

    .footer-wrapper .footer-list {
        position: absolute;
        top: 32px;
        left: 0px;
    }

    .footer-wrapper .footer-list a {
        margin-right: 15px;
    }

    .footer-wrapper .footer-units {
        position: absolute;
        top: 75px;
        left: 0px;
    }

    .footer-wrapper .footer-media {
        position: absolute;
        top: 32px;
        left: 844px;
    }
    

    .footer-wrapper .footer-media a {
        position: relative;
        display: inline-block;
        margin-right: 30px;
        vertical-align: top;
    }

    .footer-wrapper .footer-media img {
        display: none;
        position: absolute;
        top: -20px;
        left: -85px;
    }

    .footer-wrapper .footer-media a:hover {
        text-decoration: none;
    }
    
    .footer-wrapper .footer-media a:hover img{
        display: block;
    }

    .footer-wrapper .footer-media .iconfont {
        margin-right: 5px;
        font-size: 20px;
        vertical-align: middle;
    }

    .footer-wrapper .footer-msg {
        position: absolute;
        top: 75px;
        left: 844px;
    }
</style>
<div class="footer-wrapper">
    <div class="footer">
        <div class="footer-list">
            <a href="//www.chsi.com.cn/" target="_blank">学信网</a>
            <a href="https://chesicc.chsi.com.cn/zxgw/zxjs/201604/20160418/1529506207.html" target="_blank">中心简介</a>
            <a href="//www.chsi.com.cn/about/contact.shtml" target="_blank">联系我们</a>
            <a href="//www.chsi.com.cn/about/copyright.shtml" target="_blank">版权声明</a>
            <a href="/sitemap.jsp" target="_blank">网站地图</a>
            <a href="/help/" target="_blank">帮助中心</a>
            <a href="//www.chsi.com.cn/ad/index.shtml" target="_blank">网站宣传</a>
        </div>
        <div class="footer-units">
            主办单位：<a href="https://chesicc.chsi.com.cn/" target="_blank">全国高等学校学生信息咨询与就业指导中心</a><br>
            Copyright © 2003-2022 <a href="//www.chsi.com.cn/" target="_blank">学信网</a> All Rights Reserved<br>
            <a href="http://beian.miit.gov.cn" target="_blank">京ICP备19004913号-1</a>
            <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010202009747" target="_blank">
                <img src="https://t1.chei.com.cn/chsi/images/jgwab.png" style="vertical-align: middle; margin-bottom: 2px; margin-left: 8px;">
                京公网安备11010202009747号
            </a>
        </div>
        <div class="footer-media">
            <a href="javascript:;"><i class="iconfont" title="官方微信">&#xe694;</i>官方微信<img src="/news/file.do?method=downFile&amp;id=1537666622"></a>
            <a href="http://weibo.com/chsigk" target="_blank"><i class="iconfont" title="官方微博">&#xe693;</i>官方微博</a>
        </div>
        <div class="footer-msg">
            客服热线：010-67410388<br>
            客服邮箱：kefu#chsi.com.cn（将#替换为@）
        </div>
    </div>
</div>



<script src="https://t1.chei.com.cn/common/plugins/layer/layer.js"></script>
<script src="https://t1.chei.com.cn/common/plugins/placeholder-fix.js"></script>
<script src="https://t1.chei.com.cn/common/ch/browser/least-ie8.min.js"></script>
<div id="share"></div>

<script>
$(function(){
    var s = new SnsShare("share","anonymous");
    s.show();
    var gtt = new CreatGoToTop("jsGoToTop");
    gtt.goToTop();
    $('.js-alert-myd').click(function(){
        var schId = $(this).attr('data-id'),
            msgTitle = $.trim($(this).parent().siblings('.js-yxk-yxmc').text());
        $.post('/sch/yxmyd.do',{'schId':schId},function(html){
            layer.open({
                title: msgTitle,
                area: '630px',
                skin: 'layui-layer-gaokao',
                btn: '关闭',
                btnAlign: 'c',
                content: html
            });
        });
    });
});
</script>
</body>
</html>'''

html = etree.HTML(htmlCONTONT)
print(type(html))

tads = html.xpath("//table/tbody/tr/td[contains(@class,'js-yxk-yxmc'）]/a/@href")

for ta in tads:
  print(ta)

