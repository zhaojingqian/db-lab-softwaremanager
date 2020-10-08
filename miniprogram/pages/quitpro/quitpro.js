// pages/quitpro/quitpro.js
Page({

  cancel:function(option){
    wx.showModal({
      cancelColor: 'rgb(168, 205, 230)',
      content:'确认退出吗？？？',
      success(res){
          if(res.confirm){
            wx.showToast({
              title: '成功退出啦！',
              duration: 3000
            }),
            setTimeout(function() {
              //要延时执行的代码
              wx.switchTab({
              url: '../mine/mine',
            })
            }, 1000) //延迟时间
            
          }
      }
    })
  },

  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})