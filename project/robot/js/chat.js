$(function () {
    var $main = $('.main');
    var $list = $('.talk_list');
    var $mainh = $main.outerHeight(false);
    var $listh = $list.outerHeight(false);
    var $rate = $mainh / $listh;
    var $dragh = $mainh * $rate;
    var $top = 0;
    var flag = false;

    function resetui(){
        $list.children().filter(":last").get(0).scrollIntoView();
    }
    window.resetui = resetui;
})

$(function () {
 //Initialize Right Scroll Bar
//This method is defined in scroll.js
  resetui()

 //Bind mouse click events for send buttons
  $('#btnSend').on('click', function () {
    var text = $('#ipt').val().trim()
    if (text.length <= 0) {
      return $('#ipt').val('')
    }
    //If the user enters chat content, the chat content will be added to the page for display
    $('#talk_list').append('<li class="right_word"><img src="img/person02.png" /> <span>' + text + '</span></li>')
    $('#ipt').val('')
 //Reset the position of the scroll bar
    resetui()
  //Initiate a request to obtain chat content
    getMsg(text)
  })

//Obtain messages sent back by chat robots
  function getMsg(text) {
    $.ajax({
      method: 'GET',
      url: 'http://www.liulongbin.top:3006/api/robot',
      data: {
        spoken: text
      },
      success: function (res) {
        // console.log(res)
        if (res.message === 'success') {
       //Receive chat messages
          var msg = res.data.info.text
          $('#talk_list').append('<li class="left_word"><img src="img/person01.png" /> <span>' + msg + '</span></li>')
//Reset the position of the scroll bar
          resetui()
 //Call the getVoice function to convert text into speech
          getVoice(msg)
        }
      }
    })
  }
//Convert text to speech for playback
  function getVoice(text) {
    $.ajax({
      method: 'GET',
      url: 'http://www.liulongbin.top:3006/api/synthesize',
      data: {
        text: text
      },
      success: function (res) {
        // console.log(res)
        if (res.status === 200) {
         //Play voice
          $('#voice').attr('src', res.voiceUrl)
        }
      }
    })
  }

//Bind keyup event for text box
  $('#ipt').on('keyup', function (e) {
    // console.log(e.keyCode)
    if (e.keyCode === 13) {
//Console. log ('User Bounced Enter ')
      $('#btnSend').click()
    }
  })
})



