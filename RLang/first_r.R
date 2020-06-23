# rnorm(���Ժ���) �������� ����, plot�� �׸� �׷��ֱ� 
# plot(rnorm(100))

mean(anscombe$x1)
mean(anscombe$y1)

lm(y1~x1, data=anscombe)
lm(y2~x2, data=anscombe)

plot(anscombe$x1, anscombe$y1, col='red', pch=20)
plot(anscombe$x2, anscombe$y2)

par(mfrow=c(1,1))
abline(lm(y1~x1, data=anscombe), col='blue')
plot(anscombe$x2, anscombe$y2)